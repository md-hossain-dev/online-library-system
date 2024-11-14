# Use the official Python 3.12 image as the base
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the working directory
COPY . /app/

# Expose port 8000 for the Daphne server
EXPOSE 8000

# Run Django migrations and start Daphne
CMD ["sh", "-c", "python manage.py migrate && daphne -b 0.0.0.0 -p 8000 online_library_system.asgi:application"]




