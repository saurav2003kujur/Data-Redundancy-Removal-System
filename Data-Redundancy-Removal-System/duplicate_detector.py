from rapidfuzz import fuzz
from database import get_all_employees
from config import SIMILARITY_THRESHOLD

def check_exact_duplicate(email, phone):

    records = get_all_employees()

    for record in records:

        db_email = record[2]
        db_phone = record[3]

        if email == db_email:
            return True, "Duplicate Email"

        if phone == db_phone:
            return True, "Duplicate Phone"

    return False, "Unique"

def check_false_positive(name):

    records = get_all_employees()

    for record in records:

        db_name = record[1]

        score = fuzz.ratio(
            name.lower(),
            db_name.lower()
        )

        if score >= SIMILARITY_THRESHOLD:
            return True, f"Possible False Positive ({score}%)"

    return False, "Unique"