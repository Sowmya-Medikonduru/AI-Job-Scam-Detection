def detect_scam_indicators(text):
    scam_patterns = {
        "registration fee": 25,
        "processing fee": 20,
        "security deposit": 25,
        "pay money": 25,
        "pay to get job": 30,
        "send money": 25,
        "guaranteed job": 20,
        "guaranteed salary": 15,
        "no interview": 20,
        "urgent hiring": 10,
        "whatsapp only": 15,
        "telegram only": 15,
        "bank details": 25,
        "otp": 30,
        "upi payment": 25,
        "credit card details": 30,
        "password": 30,
        "aadhaar": 20,
        "pan card": 20,
        "pay for training": 20,
        "limited vacancies": 10,
        "work from home guaranteed": 15
    }

    text_lower = text.lower()
    found_indicators = []
    risk_score = 0

    for pattern, score in scam_patterns.items():
        if pattern in text_lower:
            found_indicators.append(pattern)
            risk_score += score

    risk_score = min(risk_score, 100)

    if risk_score >= 60:
        risk_level = "High Risk"
    elif risk_score >= 30:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    return found_indicators, risk_score, risk_level