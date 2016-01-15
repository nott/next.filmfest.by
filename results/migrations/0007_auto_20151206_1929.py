# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_add_results_12_13_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmpage',
            name='city_be',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='filmpage',
            name='city_en',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='filmpage',
            name='city_ru',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='filmpage',
            name='country',
            field=models.CharField(default='', max_length=2, choices=[(b'AD', 'Andorra'), (b'AE', 'United Arab Emirates'), (b'AF', 'Afghanistan'), (b'AG', 'Antigua & Barbuda'), (b'AI', 'Anguilla'), (b'AL', 'Albania'), (b'AM', 'Armenia'), (b'AN', 'Netherlands Antilles'), (b'AO', 'Angola'), (b'AQ', 'Antarctica'), (b'AR', 'Argentina'), (b'AS', 'American Samoa'), (b'AT', 'Austria'), (b'AU', 'Australia'), (b'AW', 'Aruba'), (b'AZ', 'Azerbaijan'), (b'BA', 'Bosnia and Herzegovina'), (b'BB', 'Barbados'), (b'BD', 'Bangladesh'), (b'BE', 'Belgium'), (b'BF', 'Burkina Faso'), (b'BG', 'Bulgaria'), (b'BH', 'Bahrain'), (b'BI', 'Burundi'), (b'BJ', 'Benin'), (b'BM', 'Bermuda'), (b'BN', 'Brunei Darussalam'), (b'BO', 'Bolivia'), (b'BR', 'Brazil'), (b'BS', 'Bahama'), (b'BT', 'Bhutan'), (b'BV', 'Bouvet Island'), (b'BW', 'Botswana'), (b'BY', 'Belarus'), (b'BZ', 'Belize'), (b'CA', 'Canada'), (b'CC', 'Cocos (Keeling) Islands'), (b'CF', 'Central African Republic'), (b'CG', 'Congo'), (b'CH', 'Switzerland'), (b'CI', 'Ivory Coast'), (b'CK', 'Cook Iislands'), (b'CL', 'Chile'), (b'CM', 'Cameroon'), (b'CN', 'China'), (b'CO', 'Colombia'), (b'CR', 'Costa Rica'), (b'CU', 'Cuba'), (b'CV', 'Cape Verde'), (b'CX', 'Christmas Island'), (b'CY', 'Cyprus'), (b'CZ', 'Czech Republic'), (b'DE', 'Germany'), (b'DJ', 'Djibouti'), (b'DK', 'Denmark'), (b'DM', 'Dominica'), (b'DO', 'Dominican Republic'), (b'DZ', 'Algeria'), (b'EC', 'Ecuador'), (b'EE', 'Estonia'), (b'EG', 'Egypt'), (b'EH', 'Western Sahara'), (b'ER', 'Eritrea'), (b'ES', 'Spain'), (b'ET', 'Ethiopia'), (b'FI', 'Finland'), (b'FJ', 'Fiji'), (b'FK', 'Falkland Islands (Malvinas)'), (b'FM', 'Micronesia'), (b'FO', 'Faroe Islands'), (b'FR', 'France'), (b'FX', 'France, Metropolitan'), (b'GA', 'Gabon'), (b'GB', 'United Kingdom (Great Britain)'), (b'GD', 'Grenada'), (b'GE', 'Georgia'), (b'GF', 'French Guiana'), (b'GH', 'Ghana'), (b'GI', 'Gibraltar'), (b'GL', 'Greenland'), (b'GM', 'Gambia'), (b'GN', 'Guinea'), (b'GP', 'Guadeloupe'), (b'GQ', 'Equatorial Guinea'), (b'GR', 'Greece'), (b'GS', 'South Georgia and the South Sandwich Islands'), (b'GT', 'Guatemala'), (b'GU', 'Guam'), (b'GW', 'Guinea-Bissau'), (b'GY', 'Guyana'), (b'HK', 'Hong Kong'), (b'HM', 'Heard & McDonald Islands'), (b'HN', 'Honduras'), (b'HR', 'Croatia'), (b'HT', 'Haiti'), (b'HU', 'Hungary'), (b'ID', 'Indonesia'), (b'IE', 'Ireland'), (b'IL', 'Israel'), (b'IN', 'India'), (b'IO', 'British Indian Ocean Territory'), (b'IQ', 'Iraq'), (b'IR', 'Islamic Republic of Iran'), (b'IS', 'Iceland'), (b'IT', 'Italy'), (b'JM', 'Jamaica'), (b'JO', 'Jordan'), (b'JP', 'Japan'), (b'KE', 'Kenya'), (b'KG', 'Kyrgyzstan'), (b'KH', 'Cambodia'), (b'KI', 'Kiribati'), (b'KM', 'Comoros'), (b'KN', 'St. Kitts and Nevis'), (b'KP', "Korea, Democratic People's Republic of"), (b'KR', 'Korea, Republic of'), (b'KW', 'Kuwait'), (b'KY', 'Cayman Islands'), (b'KZ', 'Kazakhstan'), (b'LA', "Lao People's Democratic Republic"), (b'LB', 'Lebanon'), (b'LC', 'Saint Lucia'), (b'LI', 'Liechtenstein'), (b'LK', 'Sri Lanka'), (b'LR', 'Liberia'), (b'LS', 'Lesotho'), (b'LT', 'Lithuania'), (b'LU', 'Luxembourg'), (b'LV', 'Latvia'), (b'LY', 'Libyan Arab Jamahiriya'), (b'MA', 'Morocco'), (b'MC', 'Monaco'), (b'MD', 'Moldova, Republic of'), (b'MG', 'Madagascar'), (b'MH', 'Marshall Islands'), (b'ML', 'Mali'), (b'MN', 'Mongolia'), (b'MM', 'Myanmar'), (b'MO', 'Macau'), (b'MP', 'Northern Mariana Islands'), (b'MQ', 'Martinique'), (b'MR', 'Mauritania'), (b'MS', 'Monserrat'), (b'MT', 'Malta'), (b'MU', 'Mauritius'), (b'MV', 'Maldives'), (b'MW', 'Malawi'), (b'MX', 'Mexico'), (b'MY', 'Malaysia'), (b'MZ', 'Mozambique'), (b'NA', 'Namibia'), (b'NC', 'New Caledonia'), (b'NE', 'Niger'), (b'NF', 'Norfolk Island'), (b'NG', 'Nigeria'), (b'NI', 'Nicaragua'), (b'NL', 'Netherlands'), (b'NO', 'Norway'), (b'NP', 'Nepal'), (b'NR', 'Nauru'), (b'NU', 'Niue'), (b'NZ', 'New Zealand'), (b'OM', 'Oman'), (b'PA', 'Panama'), (b'PE', 'Peru'), (b'PF', 'French Polynesia'), (b'PG', 'Papua New Guinea'), (b'PH', 'Philippines'), (b'PK', 'Pakistan'), (b'PL', 'Poland'), (b'PM', 'St. Pierre & Miquelon'), (b'PN', 'Pitcairn'), (b'PR', 'Puerto Rico'), (b'PT', 'Portugal'), (b'PW', 'Palau'), (b'PY', 'Paraguay'), (b'QA', 'Qatar'), (b'RE', 'Reunion'), (b'RO', 'Romania'), (b'RU', 'Russian Federation'), (b'RW', 'Rwanda'), (b'SA', 'Saudi Arabia'), (b'SB', 'Solomon Islands'), (b'SC', 'Seychelles'), (b'SD', 'Sudan'), (b'SE', 'Sweden'), (b'SG', 'Singapore'), (b'SH', 'St. Helena'), (b'SI', 'Slovenia'), (b'SJ', 'Svalbard & Jan Mayen Islands'), (b'SK', 'Slovakia'), (b'SL', 'Sierra Leone'), (b'SM', 'San Marino'), (b'SN', 'Senegal'), (b'SO', 'Somalia'), (b'SR', 'Suriname'), (b'ST', 'Sao Tome & Principe'), (b'SV', 'El Salvador'), (b'SY', 'Syrian Arab Republic'), (b'SZ', 'Swaziland'), (b'TC', 'Turks & Caicos Islands'), (b'TD', 'Chad'), (b'TF', 'French Southern Territories'), (b'TG', 'Togo'), (b'TH', 'Thailand'), (b'TJ', 'Tajikistan'), (b'TK', 'Tokelau'), (b'TM', 'Turkmenistan'), (b'TN', 'Tunisia'), (b'TO', 'Tonga'), (b'TP', 'East Timor'), (b'TR', 'Turkey'), (b'TT', 'Trinidad & Tobago'), (b'TV', 'Tuvalu'), (b'TW', 'Taiwan, Province of China'), (b'TZ', 'Tanzania, United Republic of'), (b'UA', 'Ukraine'), (b'UG', 'Uganda'), (b'UM', 'United States Minor Outlying Islands'), (b'US', 'United States of America'), (b'UY', 'Uruguay'), (b'UZ', 'Uzbekistan'), (b'VA', 'Vatican City State (Holy See)'), (b'VC', 'St. Vincent & the Grenadines'), (b'VE', 'Venezuela'), (b'VG', 'British Virgin Islands'), (b'VI', 'United States Virgin Islands'), (b'VN', 'Viet Nam'), (b'VU', 'Vanuatu'), (b'WF', 'Wallis & Futuna Islands'), (b'WS', 'Samoa'), (b'YE', 'Yemen'), (b'YT', 'Mayotte'), (b'YU', 'Yugoslavia'), (b'ZA', 'South Africa'), (b'ZM', 'Zambia'), (b'ZR', 'Zaire'), (b'ZW', 'Zimbabwe'), (b'ZZ', 'Other')]),  # noqa
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filmpage',
            name='duration_be',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filmpage',
            name='duration_en',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filmpage',
            name='duration_ru',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filmpage',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
