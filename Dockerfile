FROM mirumee/saleor:latest

COPY wsgi/ /app/saleor/wsgi/
COPY templates/ /app/templates/
