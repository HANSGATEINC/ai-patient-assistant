
import streamlit as st

mock_patient = {
    "id": "patient-001",
    "name": "Michael Baker",
    "dob": "1960-04-22",
    "gender": "M",
    "admission_date": "2025-06-15",
    "problems": [
        {
            "code": "I10",
            "label": "Essential hypertension",
            "onset": "2018-02-10"
        },
        {
            "code": "E11",
            "label": "Type 2 diabetes mellitus",
            "onset": "2015-07-02"
        },
        {
            "code": "N18.3",
            "label": "Chronic kidney disease, stage 3",
            "onset": "2021-09-20"
        }
    ],
    "medications": [
        {
            "name": "Metformin",
            "dose": "500 mg BID",
            "start": "2015-07-03",
            "end": "Present"
        },
        {
            "name": "Lisinopril",
            "dose": "20 mg daily",
            "start": "2018-02-11",
            "end": "Present"
        },
        {
            "name": "Furosemide",
            "dose": "40 mg daily",
            "start": "2025-06-15",
            "end": "Present"
        }
    ],
    "labs": [
        {
            "test": "Creatinine",
            "value": 1.3,
            "unit": "mg/dL",
            "date": "2025-06-15"
        },
        {
            "test": "HbA1c",
            "value": 7.8,
            "unit": "%",
            "date": "2025-06-14"
        },
        {
            "test": "Potassium",
            "value": 4.2,
            "unit": "mmol/L",
            "date": "2025-06-15"
        }
    ],
    "procedures": [
        {
            "name": "EKG",
            "date": "2025-06-15",
            "result": "Sinus rhythm, no acute changes"
        },
        {
            "name": "Ultrasound Abdomen",
            "date": "2025-06-16",
            "result": "No biliary obstruction"
        }
    ],
    "notes": [
        {
            "date": "2025-06-15",
            "author": "Dr. Lee (Hospitalist)",
            "text": "Admitted for volume overload and elevated creatinine. History of CKD stage 3\u2026"
        },
        {
            "date": "2025-06-16",
            "author": "Dr. Patel (Nephrology)",
            "text": "Recommend adjusting lisinopril dose and reinforcing loop diuretic regimen\u2026"
        }
    ]
}

question_map = {
    "creatinine": lambda p: f"Latest creatinine: {p['labs'][0]['value']} {p['labs'][0]['unit']} on {p['labs'][0]['date']}.",
    "medications": lambda p: "Current medications:\n" + "\n".join(
        [f"- {m['name']} ({m['dose']})" for m in p['medications']]),
    "nephrology": lambda p: p['notes'][1]['text'],
    "hospitalist": lambda p: p['notes'][0]['text'],
    "procedures": lambda p: "Recent procedures:\n" + "\n".join(
        [f"- {proc['name']} on {proc['date']}: {proc['result']}" for proc in p['procedures']])
}

st.title("AI Assistant (Realistic Patient Mode)")
st.write("Selected patient: **Michael Baker (M, 1960-04-22)**")

question = st.text_input("Ask a clinical question (e.g., What is the latest creatinine?)")

if question:
    q = question.lower()
    response = "I'm sorry, I couldn't find an answer."
    for keyword, func in question_map.items():
        if keyword in q:
            response = func(mock_patient)
            break

    st.markdown(f"**AI Response:**\n\n{response}")
