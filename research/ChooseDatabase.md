# Research Task: Choosing Between SQLite or JSON for Data Storage

## Why I am doing it
This research is being conducted to determine the best data storage solution for the Bullet Journal app.
Choosing between SQLite and JSON is critical for ensuring efficient storage and retrieval of user data
like journal entries, preferences, and personal information. It will also affect how the data is structured,
accessed, and maintained throughout the project.

## What I expect to learn/do
Compare the two in terms of simplicity of implementation, data handling efficiency, and future scalability.
and learn the differences between SQLite and JSON in terms of:
- Performance for handling a growing number of journal entries.
- Integration ease with Flask.
- Flexibility for future schema changes or new features.

## What I expect to do with it
The decision from this research will dictate which storage method is used for the project:
- If **SQLite** is chosen, I will implement the database models using SQLAlchemy and set up tables for users, journal entries, and preferences.
- If **JSON** is chosen, I will develop a module that handles file I/O for storing and retrieving data in JSON format.

## Code/Modules Affected
- **Database Configuration Module**: This module will be designed to manage the chosen storage method, either through SQLite or JSON.
- **Journal & User Management**: Modules that create, read, update, and delete user preferences and journal entries will rely on the storage solution selected.

## Final Decision: SQLite
After completing the research, **SQLite** has been chosen as the storage solution for the Bullet Journal app. The following factors influenced the decision:
- **Security**: SQLite offers better support for secure data storage, with options for encryption that ensure user data is protected.
- **Performance**: SQLite is more efficient for handling larger datasets and offers scalability as the number of journal entries and users increases.
- **Ease of Integration**: SQLite integrates seamlessly with Flask via SQLAlchemy, allowing for cleaner database management and straightforward migration capabilities.
- **Flexibility**: SQLite's structured query language provides the ability to run complex queries, making it more suitable for handling user preferences and journal entry search functionality.

## Code/Modules Impacted by the Decision
- **Database Configuration**: I will create and configure the SQLite database using SQLAlchemy within the Flask app.
- **Journal & User Management**: CRUD operations will be built using SQLAlchemy models to store and retrieve user data and journal entries.

## Jira Tasks Dependent on Research
- Task 2: Design the data schema for journal entries, preferences, and user information.
- Task 3: Implement the database setup and configuration within Flask.
- Task 4: Implement CRUD operations for journal entries and user preferences.
