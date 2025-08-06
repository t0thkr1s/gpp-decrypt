FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Install the package
RUN pip install --no-cache-dir .

# Create a non-root user
RUN useradd -m -u 1000 gppuser && chown -R gppuser:gppuser /app
USER gppuser

# Set entrypoint
ENTRYPOINT ["gpp-decrypt"]
