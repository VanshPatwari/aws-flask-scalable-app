# AWS Scalable Flask App 🚀

## 📌 Overview

This project demonstrates deployment of a scalable web application on AWS with Infrastructure as Code and CI/CD automation.

---

## 🏗️ Architecture

Terraform → EC2 → Flask App → RDS (MySQL) → API → Internet
CI/CD via GitHub Actions

---

## 🔧 Tech Stack

* AWS EC2
* AWS RDS (MySQL)
* Application Load Balancer
* GitHub Actions (CI/CD)
* Terraform (Infrastructure as Code)
* Python Flask

---

## ⚙️ Infrastructure (Terraform)

* Provisioned EC2 instance using Terraform
* Created Security Groups for controlled access
* Automated infrastructure setup instead of manual deployment

---

## 🔐 Security

* Used environment variables (no hardcoded credentials)
* Configured Security Groups for restricted DB access

---

## 🚀 How to Run

1. Clone repo

2. Set environment variables:

   * DB_HOST
   * DB_USER
   * DB_PASSWORD
   * DB_NAME

3. Run:

```
python3 app.py
```

---

## 📸 Demo
<img width="872" height="401" alt="image" src="https://github.com/user-attachments/assets/c6732c3d-7939-4dd7-82ee-d205953b3747" />


### API Response

(Add Postman / browser screenshot here)

---

## 📈 Key Learnings

* Cloud deployment & networking (VPC, Security Groups)
* Infrastructure as Code using Terraform
* CI/CD automation using GitHub Actions
* Debugging real-world production issues
