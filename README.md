
readme_content = """# 📇 Contact Manager CLI

A minimal JSON-based contact manager built in Python for **Phase 1 – Python Intermediate | Day 2**.

## What It Does

- ➕ Add contacts (name + phone)
- 🔍 Search contacts by exact name
- 💾 Auto-saves to `contacts.json`
- 📂 Auto-loads on startup (creates file if missing)

## Run It

```bash
python contact_manager.py
```

## Concepts Used

| Concept | Where |
|---------|-------|
| `open()` | Reading/writing `contacts.json` |
| `json.load()` | Loading saved contacts |
| `json.dump()` | Saving contacts with pretty print |
| `os.path.exists()` | Checking if file exists before opening |
| `with` statement | Safe file handling |
| `try/except` | Graceful handling of corrupted/empty files |

## File Structure

```
contact_manager.py
contacts.json     # auto-generated
```

## Example

```
[ Menu ]
1. Add a new contact
2. Search for a contact
3. Exit
Choose an option (1-3): 1
Enter contact name: Alice
Enter phone number: 555-0123
✔️ Successfully saved Alice!
```

## Notes

- Search is case-sensitive and exact-match
- Each contact stores one phone number only
- No edit/delete functionality (Day 2 scope)

