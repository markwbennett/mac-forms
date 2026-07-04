# mac-forms

Generates `texas_habeas_questionnaire.pdf`, a client intake questionnaire for Texas postconviction habeas corpus matters (Tex. Code Crim. Proc. arts. 11.07, 11.072, 11.08, 11.09), built with reportlab.

## Run

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_habeas_questionnaire.py
```

Output is written to `texas_habeas_questionnaire.pdf` in the current directory.
