import gradio as gr
import pandas as pd
import joblib
import pickle

model = joblib.load("models/rfc_manual_selection.joblib")

with open("models/categorical_features_manual_selection.pkl", "rb") as f:
    categorical_features = pickle.load(f)


def feat_eng(df):
    df = df.copy()
    # Create a column of percentage of exams approved
    df = df.assign(
        # Number of approved units over total number of evaluations (its not a percentage of approved exams)
        first_sem_approved_over_evaluations=lambda x: x.first_sem_approved / x.first_sem_evaluations,
        second_sem_approved_over_evaluations=lambda x: x.second_sem_approved / x.second_sem_evaluations,
        # There are some students with 0 evaluations in the semesters, the coefficient will be np.nan value.
        # I will fill these with the mean value and create a boolean flag
        first_sem_has_evals=lambda x: x.first_sem_evaluations != 0,
        second_sem_has_evals=lambda x: x.second_sem_evaluations != 0,
        # Boolean flag for sem_without_evaluations predictors
        first_sem_has_units_without_evals=lambda x: x.first_sem_without_evaluations == 0,
        second_sem_has_units_without_evals=lambda x: x.second_sem_without_evaluations == 0,
        # Ratio of average grade over number of enrolled units
        first_sem_grade_over_enrolled=lambda x: x.first_sem_grade / x.first_sem_enrolled,
        second_sem_grade_over_enrolled=lambda x: x.second_sem_grade / x.second_sem_enrolled,
        # Again, there are some students with 0 enrolled units in the semesters, the coefficient will be np.nan value.
        # I will fill these with the mean value and create a boolean flag
        first_sem_has_enrolled=lambda x: x.first_sem_enrolled != 0,
        second_sem_has_enrolled=lambda x: x.second_sem_enrolled != 0,
        # Number of disapproved units
        first_sem_disapproved=lambda x: x.first_sem_enrolled - x.first_sem_approved,
        second_sem_disapproved=lambda x: x.second_sem_enrolled - x.second_sem_approved,
        # Percentage of units credited over enrolled
        first_sem_perc_credited=lambda x: x.first_sem_credited / x.first_sem_enrolled,
        second_sem_perc_credited=lambda x: x.second_sem_credited / x.second_sem_enrolled,
    )
    return df


def predict(*args):
    names = [
        "course",
        "day_evening",
        "previous_education",
        "displaced",
        "tuition_fees_up_to_date",
        "gender",
        "scholarship_holder",
        "age_at_enrollment",
        "first_sem_credited",
        "first_sem_enrolled",
        "first_sem_evaluations",
        "first_sem_approved",
        "first_sem_grade",
        "first_sem_without_evaluations",
        "second_sem_credited",
        "second_sem_enrolled",
        "second_sem_evaluations",
        "second_sem_approved",
        "second_sem_grade",
        "second_sem_without_evaluations",
    ]
    df = pd.DataFrame([args], columns=names)
    df = df.pipe(feat_eng)
    prediction = model.predict_proba(df)
    return {"Not Dropout": prediction[0][0], "Dropout": prediction[0][1]}


with gr.Blocks() as demo:
    gr.Markdown(
        """
    # Analysis of students dropout and academic success
    
    Predicting probability of students dropout
    """
    )
    with gr.Row():
        with gr.Column():
            course = gr.Dropdown(label="Course", choices=categorical_features["course"])
            day_evening = gr.Dropdown(label="Day/Evening", choices=categorical_features["day_evening"])
            previous_education = gr.Dropdown(
                label="Previous education", choices=categorical_features["previous_education"]
            )
            displaced = gr.Dropdown(label="Displaced", choices=categorical_features["displaced"])
            tuition_fees_up_to_date = gr.Dropdown(
                label="Tuition fees up to date?", choices=categorical_features["tuition_fees_up_to_date"]
            )
            gender = gr.Dropdown(label="Gender", choices=categorical_features["gender"])
            scholarship_holder = gr.Dropdown(
                label="Scholarship holder?", choices=categorical_features["scholarship_holder"]
            )
            age_at_enrollment = gr.Number(label="Age at time of enrollment")
        with gr.Column():
            first_sem_credited = gr.Number(label="Curricular units 1st sem (credited)")
            first_sem_enrolled = gr.Number(label="Curricular units 1st sem (enrolled)")
            first_sem_evaluations = gr.Number(label="Curricular units 1st sem (evaluations)")
            first_sem_approved = gr.Number(label="Curricular units 1st sem (approved)")
            first_sem_grade = gr.Number(label="Curricular units 1st sem (grade)")
            first_sem_without_evaluations = gr.Number(label="Curricular units 1st sem (without evaluations)")
        with gr.Column():
            second_sem_credited = gr.Number(label="Curricular units 2nd sem (credited)")
            second_sem_enrolled = gr.Number(label="Curricular units 2nd sem (enrolled)")
            second_sem_evaluations = gr.Number(label="Curricular units 2nd sem (evaluations)")
            second_sem_approved = gr.Number(label="Curricular units 2nd sem (approved)")
            second_sem_grade = gr.Number(label="Curricular units 2nd sem (grade)")
            second_sem_without_evaluations = gr.Number(label="Curricular units 2nd sem (without evaluations)")
    with gr.Row():
        with gr.Column():
            predict_btn = gr.Button(value="Predict")
        with gr.Column():
            label = gr.Label(label="Outcome probabilities", show_label=False)
            predict_btn.click(
                predict,
                inputs=[
                    course,
                    day_evening,
                    previous_education,
                    displaced,
                    tuition_fees_up_to_date,
                    gender,
                    scholarship_holder,
                    age_at_enrollment,
                    first_sem_credited,
                    first_sem_enrolled,
                    first_sem_evaluations,
                    first_sem_approved,
                    first_sem_grade,
                    first_sem_without_evaluations,
                    second_sem_credited,
                    second_sem_enrolled,
                    second_sem_evaluations,
                    second_sem_approved,
                    second_sem_grade,
                    second_sem_without_evaluations,
                ],
                outputs=[label],
            )

            # )
            # with gr.Row():
            #     predict_btn = gr.Button(value="Predict")
            #     interpret_btn = gr.Button(value="Explain")
            # predict_btn.click(
            #     predict,
            #     inputs=[
            #         age,
            #         work_class,
            #         education,
            #         years,
            #         marital_status,
            #         occupation,
            #         relationship,
            #         sex,
            #         capital_gain,
            #         capital_loss,
            #         hours_per_week,
            #         country,
            #     ],
            #     outputs=[label],
            # )
            # interpret_btn.click(
            #     interpret,
            #     inputs=[
            #         age,
            #         work_class,
            #         education,
            #         years,
            #         marital_status,
            #         occupation,
            #         relationship,
            #         sex,
            #         capital_gain,
            #         capital_loss,
            #         hours_per_week,
            #         country,
            #     ],
            #     outputs=[plot],
            # )

demo.launch()
