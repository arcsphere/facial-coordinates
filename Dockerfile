# *******************************************
# **** Assignment submission by Arjun Shrivatsan
# **** EAI 6010 - Assignment No: Facial Coordinate Identification - Deployment
# *******************************************

FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install OS-level dependencies including OpenGL (libGL)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the full app directory into the container
COPY . .

# Run the app
CMD ["python", "app.py"]
