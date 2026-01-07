FROM python:3.13-slim 

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set work directory
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies first (for caching)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

COPY . .


EXPOSE 8000
RUN chmod +x /app/entry_point.sh
# Run the app with Gunicorn
CMD ["/app/entry_point.sh"]