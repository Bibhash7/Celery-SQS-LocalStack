from celery_app import add

if __name__ == "__main__":
    result = add.delay(4, 6)
    print(f"Task result: {result.get(timeout=5)}")
