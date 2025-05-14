# Берём официальный образ RabbitMQ, который уже основан на Debian
FROM rabbitmq:3.12-management-alpine

LABEL maintainer="your-email@example.com"

# Можно добавить кастомные настройки, например:
COPY rabbitmq.conf /etc/rabbitmq/

EXPOSE 5672 15672

CMD ["rabbitmq-server"]
