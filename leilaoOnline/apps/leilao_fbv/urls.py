from django.shortcuts import redirect
from django.urls import path

from leilao_fbv import views

app_name = 'leilao_fbv'

urlpatterns = [

	##############################################################################
	### Lote #####################################################################
	##############################################################################

	# path('', views.lote_list, name='lote_list'),
	# path('new/', views.lote_create, name='lote_new'),
	# path('edit/<int:pk>/', views.lote_update, name='lote_edit'),
	# path('delete/<int:pk>/', views.lote_delete, name='lote_delete'),

	path('', views.list_lote, name='lote_list'),
	# path('new/', views.create_lote, name='lote_new'),
	# path('edit/<int:pk>/', views.update_lote, name='lote_edit'),
	# path('delete/<int:pk>/', views.delete_lote, name='lote_delete'),

	##############################################################################
	### Perfil ###################################################################
	##############################################################################

	path('select/', views.select_perfil, name='select_perfil'),

	##############################################################################
	### Vendedor #################################################################
	##############################################################################

	# path('', views.list_vendedor, name='vendedor_list'),
	# path('user_page/', views.redirect_vendedor, name='redirect_vendedor'),
	path('signup_vendedor/', views.create_vendedor, name='vendedor_new'),
	#path('/', views.create_vendedor, name='vendedor_new'),
	# path('edit/<int:pk>/', views.update_vendedor, name='vendedor_edit'),
	# path('delete/<int:pk>/', views.delete_vendedor, name='vendedor_delete'),

	##############################################################################
	### Comprador ################################################################
	##############################################################################

	# path('', views.list_comprador, name='comprador_list'),
	# path('user_page/', views.redirect_comprador, name='redirect_comprador'),
	path('signup_comprador/', views.create_comprador, name='comprador_new'),
	# path('edit/<int:pk>/', views.update_comprador, name='comprador_edit'),
	# path('delete/<int:pk>/', views.delete_comprador, name='comprador_delete'),

	##############################################################################
	### Leiloeiro ################################################################
	##############################################################################

	path('signup_leiloeiro/', views.create_leiloeiro, name='leiloeiro_new'),
]