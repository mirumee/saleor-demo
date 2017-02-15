FROM mirumee/saleor:latest

COPY wsgi/ /app/saleor/wsgi/
COPY /app/templates/base.html /app/templates/base_original.html
COPY /app/templates/dashboard/base.html /app/templates/dashboard/base_original.html
COPY templates/ /app/templates/
