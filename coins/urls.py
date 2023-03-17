from django.urls import path

from coins.views import wallets_view, coin_details_view, portfolio, generate_data


urlpatterns = [
    path('', coin_details_view, name='coin_details'),
    path('wallets/', wallets_view, name='wallets'),
    path('portfolio/', portfolio, name='portfolio'),
    path('generate-data/', generate_data, name='generate_data'),
]