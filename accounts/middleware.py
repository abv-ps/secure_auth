import logging
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)


class LogAccessMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path
        user = request.user
        ip_address = self.get_client_ip(request)

        # Список захищених префіксів URL (можете налаштувати)
        protected_prefixes = ['/profile/', '/dashboard/', '/admin/']

        # Список "підозрілих" URL (можете налаштувати)
        suspicious_urls = ['/admin/', '/administrator/', '/wp-admin/', '.git']

        is_protected = any(path.startswith(prefix) for prefix in protected_prefixes)
        is_suspicious = any(url in path for url in suspicious_urls)

        if is_protected:
            if user.is_authenticated:
                logger.warning(f"AUTH USER: {user}, IP: {ip_address}, accessed protected: {path}")
            else:
                logger.warning(f"UNAUTH USER, IP: {ip_address}, attempted access to protected: {path}")
        elif is_suspicious:
            logger.warning(f"SUSPICIOUS ACCESS ATTEMPT, IP: {ip_address}, path: {path}")

        return None

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class CustomErrorMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(f"Error occurred: {exception}", exc_info=True)  # Логуємо помилку з трасуванням
        return render(request, 'accounts/500.html', status=500)

    def process_response(self, request, response):
        if response.status_code == 404:
            return render(request, 'accounts/404.html', status=404)
        return response
