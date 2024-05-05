import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Создание отчета (в данном случае просто загрузка и обработка CSV файла)
def create_report(data_file):
    df = pd.read_csv(data_file)
    # Здесь может быть логика создания отчета на основе данных из файла
    return df

# Функция для отправки электронной почты
def send_email(receiver_email, subject, body):
    sender_email = "your_email@example.com"
    password = "your_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

# Основная часть скрипта
if __name__ == "__main__":
    # Создание отчета
    report_data = create_report("data.csv")

    # Отправка отчета по электронной почте
    receiver_email = "recipient@example.com"
    subject = "Еженедельный отчет"
    body = "Прикреплен отчет за текущую неделю."
    send_email(receiver_email, subject, body)

    print("Задачи по созданию отчетов, рассылке писем и обработке данных автоматизированы!")
