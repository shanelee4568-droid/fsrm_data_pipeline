# Project Setup Guide

This guide details the steps required to set up and run the application on **Windows**.

---

## Prerequisites

Before starting, ensure you have `uv` installed. If you haven't installed it yet, run the following command in your PowerShell terminal:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Installation & Setup

Follow these steps in your terminal to configure the project environment:

### 1. Navigate to the Project Directory
Change your current directory to the folder containing the project files:
```bash
cd path/to/your/folder
```

### 2. Synchronize Dependencies
Install the required dependencies using `uv`:
```bash
uv sync
```

### 3. Add Input Files
Place your required **Excel input files** into the input folder.
Get access to "Nitita Chaiarsa - Stock FSRM SSC" sharepoint folder and sync to add a PATH to your laptop

### 4. Configure Environment Variables
* Rename the file `.env.example` to `.env`.
* Open `.env` in an editor and add your environment variables.

---

## Running the Application

Once the setup is complete, execute the main script:

```bash
uv run main.py
```

---

# คู่มือการตั้งค่าโปรเจกต์ (Thai Ver.)

คู่มือนี้จะอธิบายขั้นตอนที่จำเป็นในการตั้งค่าและรันแอปพลิเคชันบน **Windows**

---

## สิ่งที่ต้องเตรียมก่อนเริ่ม (Prerequisites)

ก่อนเริ่มต้น ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง `uv` เรียบร้อยแล้ว หากยังไม่ได้ติดตั้ง ให้รันคำสั่งต่อไปนี้ใน PowerShell terminal ของคุณ:

```powershell
powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```

---

## การติดตั้งและการตั้งค่า (Installation & Setup)

ทำตามขั้นตอนต่อไปนี้ใน terminal เพื่อตั้งค่าสภาพแวดล้อมของโปรเจกต์:

### 1. ไปยังโฟลเดอร์ของโปรเจกต์
เปลี่ยน directory ไปยังโฟลเดอร์ที่เก็บไฟล์โปรเจกต์:
```bash
cd path/to/your/folder
```

### 2. ซิงค์ Dependencies
ติดตั้ง dependencies ที่จำเป็นโดยใช้ `uv`:
```bash
uv sync
```

### 3. เพิ่มไฟล์ Input
* นำไฟล์ **Excel input** ที่จำเป็นไปใส่ไว้ในโฟลเดอร์ input
* ขอสิทธิ์เข้าถึงโฟลเดอร์ SharePoint "Nitita Chaiarsa - Stock FSRM SSC" และทำการซิงค์ (sync) เพื่อเชื่อมโยง PATH เข้ากับแล็ปท็อปของคุณ

### 4. ตั้งค่า Environment Variables
* เปลี่ยนชื่อไฟล์จาก `.env.example` เป็น `.env`
* เปิดไฟล์ `.env` ด้วยโปรแกรมแก้ไขข้อความ (editor) แล้วใส่ค่า environment variables ของคุณ

---

## การรันแอปพลิเคชัน (Running the Application)

เมื่อตั้งค่าทุกอย่างเสร็จเรียบร้อยแล้ว ให้รันสคริปต์หลักด้วยคำสั่งนี้:

```bash
uv run main.py
```

Extra
DAY = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]




