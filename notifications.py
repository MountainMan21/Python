from plyer import notification

def send_notification(title, message):
    print(f"Sending notification: {title} - {message}")  # Debugging line
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )
