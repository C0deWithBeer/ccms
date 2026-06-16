# 🏛️ CCMS: Community Complaint Management System

A full-stack web application built with Python and Django designed to streamline the logging, viewing, and handling of community-driven grievances. 

This project is built to demonstrate solid fundamental web development practices: database normalization, role-based conditional rendering, secure user authentication, and full CRUD flow execution.

---

## 🛠️ Project Architecture & Skills Showcased

Rather than using automated tools, this codebase explicitly builds out core workflows to master backend engineering:

### ⚡ Core Implementations
* **Relational Database Design:** Employs a one-to-many (`ForeignKey`) data relationship connecting Django's built-in `User` model to custom complaint entries.
* **Granular Role Restriction:** Custom server-side verification using Python blocks regular users from hitting specific administrative endpoints (`is_staff` checking).
* **Dynamic Context Processing:** Views dynamically toggle front-end templates depending on user sessions (`has_logged_in`).
* **Django ORM Efficiency:** Employs precise `.filter()` queries to safely segregate user data without leaking information across accounts.

---
