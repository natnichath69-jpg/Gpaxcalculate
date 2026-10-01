import json

def build():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        data = []

    # คัดเอาเฉพาะรายการที่เป็นวิชาเรียน
    subjects = [item for item in data if isinstance(item, dict) and item.get("subject")]

    return {
        "has_subjects": len(subjects) > 0,  # เพิ่มตัวแปรนี้เพื่อให้ templates/page1.html รู้ว่ามีข้อมูล
        "subjects": subjects,
        "items": subjects,
        "data": subjects,
        "rows": subjects
    }