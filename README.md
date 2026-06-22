 **📇 CLI based Contact Manager**

A minimal JSON-based contact manager built in Python.

## What It Does

- ➕ Add contacts (name + phone)
- 🔍 Search contacts by exact name
- 💾 Auto-saves to `contacts.json`
- 📂 Auto-loads on startup (creates file if missing)
Installation & Usage
Clone your repository (if you haven't already) and navigate into it:

```Bash
git clone https://github.com/your-username/unprof.git
cd unprof
```
To execute the program 
```Bash
python3 contact_manager.py
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

