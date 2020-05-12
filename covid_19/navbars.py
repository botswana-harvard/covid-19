from django.conf import settings

from edc_navbar import NavbarItem, site_navbars, Navbar

covid_19 = Navbar(name='covid_19')

covid_19.append_item(
    NavbarItem(
        name='visitor',
        title='Visitor',
        label='Visitor',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'visitor_listboard_url')))

covid_19.append_item(
    NavbarItem(
        name='employee',
        title='Employee',
        label='Employee',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'employee_listboard_url')))


site_navbars.register(covid_19)
