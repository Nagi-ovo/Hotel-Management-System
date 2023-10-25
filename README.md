# Hotel Management System DEMO

Based on [shubhank's awsome project](https://github.com/shubhank7673/hotel-management-system), db bug fixed and new features added.
## How to Run

1. `pip install -r requirements.txt`

2. Run `main.py`

## Directory Structure Description

```
📁 Useful Content
├── 📝 README.md                    // Guide
├── 📋 requirements.txt             // Library dependencies
└── 📁 Starrt-Hotel-Management-System   // Core code
    ├── 🖼️ image                     // File src
    ├── 🗄️ hm_proj.db                // SQLite database file
    ├── 📜 login_system.py           // Login system
    ├── 📜 main.py                   // Main function
    ├── 📜 MainRoot.py               // Main framework setup file
    └── 📜 test.txt                  // Password storage document
```

### Version 1.0.1 - Content Update

- [x] Fixed known bugs 🐛🐛🐛
- [x] Improved UI aesthetics 🎨

### Version 1.0.2 - Content Update

- [x] Fixed bug where previously selected payment method buttons remained selected
- [x] Fixed issue with incorrect storage of "payment method" attribute
- [x] Fixed issue with incorrect retrieval of "payment method" attribute from the database

### Version 1.1.1 - Content Update

- [x] Added "Login" interface 🔐
- [x] Added functionality to visualize attributes such as "number of rooms" correctly from the database

### Version 1.1.2 - Content Update

- [x] Fixed bug where entering incorrect password during login did not result in any punishment; now the program can be terminated properly
- [x] Improved login interface style 💻
