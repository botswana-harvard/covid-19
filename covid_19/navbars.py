from django.conf import settings

from edc_navbar import NavbarItem, site_navbars, Navbar

covid_19 = Navbar(name='covid_19')
covid_19_sites = Navbar('covid_19_sites')

covid_19.append_item(
    NavbarItem(
        name='visitor',
        title='Visitor',
        label='Visitor',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'bhp_hq_visitor_listboard_url')))

covid_19.append_item(
    NavbarItem(
        name='employee',
        title='Employee',
        label='Employee',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'bhp_hq_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='bhp_hq',
        title='BHP HQ',
        label='BHP HQ',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'bhp_hq_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='ctu',
        title='CTU',
        label='CTU',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'ctu_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='hptn',
        title='HPTN',
        label='HPTN',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'hptn_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='ambition',
        title='Ambition',
        label='Ambition',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'ambition_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='hr_finance',
        title='Finance & Human Resources',
        label='Finance & HR',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'hr_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='pepfar',
        title='PEPFAR',
        label='PEPFAR',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'pepfar_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='tsepamo',
        title='Tsepamo',
        label='Tsepamo',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'tsepamo_listboard_url')))

covid_19_sites.append_item(
    NavbarItem(
        name='mmabana',
        title='Mmabana',
        label='Mmabana',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'mmabana_listboard_url')))

covid19_visitor = Navbar(name='covid19_visitor')

covid19_visitor.append_item(
    NavbarItem(
        name='bhp_hq_visitor',
        title='BHP HQ',
        label='BHP HQ',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'bhp_hq_visitor_listboard_url')))

covid19_visitor.append_item(
    NavbarItem(
        name='ambition_visitor',
        title='Ambition',
        label='Ambition',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'ambition_visitor_listboard_url')))

covid19_visitor.append_item(
    NavbarItem(
        name='ctu_visitor',
        title='CTU',
        label='CTU',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'ctu_visitor_listboard_url')))

covid19_visitor.append_item(
    NavbarItem(
        name='hptn_visitor',
        title='HPTN',
        label='HPTN',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'hptn_visitor_listboard_url')))

covid19_visitor.append_item(
    NavbarItem(
        name='finance_hr_visitor',
        title='Finance & Human Resources',
        label='Finance & HR',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'hr_visitor_listboard_url')))

covid19_visitor.append_item(
    NavbarItem(
        name='mmabana_visitor',
        title='Mmabana',
        label='Mmabana',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'mmabana_visitor_listboard_url')))

covid19_visitor.append_item(
    NavbarItem(
        name='pepfar_visitor',
        title='PEPFAR',
        label='PEPFAR',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'pepfar_visitor_listboard_url')))

covid19_visitor.append_item(
    NavbarItem(
        name='tsepamo_visitor',
        title='Tsepamo',
        label='Tsepamo',
        url_name=settings.DASHBOARD_URL_NAMES.get(
            'tsepamo_visitor_listboard_url')))

site_navbars.register(covid_19)
site_navbars.register(covid_19_sites)
site_navbars.register(covid19_visitor)
