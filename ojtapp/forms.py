from django import forms


LAN_CHOICES = (
    ('1', '100BASE-TX,全二重'),
    ('2', '100BASE-TX,半二重'),
    ('3', '10BASE-TX,全二重'),
    ('4', '10BASE-TX,半二重'),
    ('5', '自動(100Mbps/10Mbps)'),
    ('6', '自動(10Mbps 固定)')
)

ALARM_OFF = (
    ('on','アラーム出力する'),
    ('off','アラーム出力しない')
    )

REC_link = (
    ('off','無効'),
    ('on','有効')
    
    )

SEND_link = (
    ('off','無効'),
    ('on','有効')
    
    )

RLDN_link = (
    ('off','無効'),
    ('on','有効')
    
    )

RINH_link = (
    ('off','無効'),
    ('on','有効')
    
    )

RINH = (
    ('off','無効'),
    ('on','有効')
    
    )

FEFI = (
    ('off','無効'),
    ('on','有効')
    
    )

class LanForm(forms.Form):
    lan_set = forms.ChoiceField(
        label='LAN側コネクションタイプ',
        widget=forms.RadioSelect,
        choices=LAN_CHOICES,
        required=True,
        initial=LAN_CHOICES[2]
    )

    alarm_off_set = forms.ChoiceField(
        label='ALARM_OFF',
        widget=forms.RadioSelect,
        choices=ALARM_OFF,
        required=True,
        initial=ALARM_OFF[0]
    )
    rec_link_set = forms.ChoiceField(
        label='RECリンクパススルー機能',
        widget=forms.RadioSelect,
        choices=REC_link,
        required=True,
        initial=REC_link[0]
    )
    send_link_set = forms.ChoiceField(
        label='SENDリンクパススルー機能',
        widget=forms.RadioSelect,
        choices=SEND_link,
        required=True,
        initial=SEND_link[0]
    )
    rldn_link_set = forms.ChoiceField(
        label='RLDNリンクパススルー機能',
        widget=forms.RadioSelect,
        choices=RLDN_link,
        required=True,
        initial=RLDN_link[0]
    )
    rinh_link_set = forms.ChoiceField(
        label='RINHリンクパススルー機能',
        widget=forms.RadioSelect,
        choices=RINH_link,
        required=True,
        initial=RINH_link[0]
    )
    RINH_set = forms.ChoiceField(
        label='RINH',
        widget=forms.RadioSelect,
        choices=RINH,
        required=True,
        initial=RINH[0]
    )
    FEFI_set = forms.ChoiceField(
        label='FEFI',
        widget=forms.RadioSelect,
        choices=FEFI,
        required=True,
        initial=FEFI[0]
    )