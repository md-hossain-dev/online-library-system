# Use the official Python 3.12 image as the base
FROM python:3.12

# Set environment variables to optimize Python's behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the working directory
COPY . /app/

# Install curl to download wait-for-it.sh if it's not in the local project
RUN apt-get update && apt-get install -y curl

# Download wait-for-it.sh to handle dependency wait times
RUN curl -o /app/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Expose port 8000 for the Daphne server
EXPOSE 8000

# Command to run Django migrations and then start the ASGI server with Daphne
CMD ["sh", "-c", "./wait-for-it.sh db:5432 -- python manage.py migrate && daphne -b 0.0.0.0 -p 8000 online_library_system.asgi:application"]
