from django.core.management.base import BaseCommand
from ...models import AVVendor

class Command(BaseCommand):
    help = 'Initialize AVVendor data'

    def handle(self, *args, **kwargs):
        vendors = [
            { 'name': 'Acronis', 'contact': 'https://www.acronis.com/en-us/company/contacts/ (page de contact globale)', 'comments': 'Acronis (Suisse) – backup & sécurité (voir Twitter @AcronisSupport).' },
            { 'name': 'Ad-Aware', 'contact': 'Support via portail Zendesk multilingue https://adaware.zendesk.com', 'comments': 'Ad-Aware (Lavasoft/Avanquest, Canada) – antivirus desktop; support via forum/FAQ.' },
            { 'name': 'AntiVir', 'contact': 'Portail support global Avira (English, etc.)', 'comments': 'Avira GmbH (Allemagne) – éditeur d’Avira Antiviral (marque AntiVir).' },
            { 'name': 'AhnLab', 'contact': 'Siège: 220 Pangyoyeok-ro, Bundang-gu, Seongnam (Corée), +82-31-722-8000; filial Japon (+81-3-6453-8315):contentReference[oaicite:14]{index=14}; China (cn.sales@ahnlab.com).', 'comments': 'AhnLab (Corée) – antivirus V3; contact global via site (offres multi-plateformes).' },
            { 'name': 'AhnLab V3', 'contact': 'Voir AhnLab (Corée) ci-dessus', 'comments': 'AhnLab V3 (Corée) – moteur antivirus de la suite V3 d’AhnLab.' },
            { 'name': 'Alibaba', 'contact': 'Alibaba Group (Chine) – site corporate AlibabaGroup.com (pas d’email direct connu)', 'comments': 'Alibaba (Chine) – moteur antivirus axé sur mobile/Android.' },
            { 'name': 'AlibabaCloud', 'contact': 'Alibaba Cloud (https://www.alibabacloud.com) via formulaires de contact', 'comments': 'Alibaba Cloud (division Alibaba, Chine) – moteur antivirus intégré à Security Center.' },
            { 'name': 'ALYac', 'contact': 'ESTsecurity (Corée) – siège: Banpo-daero 3, Seocho-gu, Seoul', 'comments': 'ESTsecurity (Corée) – éditeur d’ALYac EDR.' },
            { 'name': 'Antiy Labs', 'contact': 'Email: support@antiy.cn; Tél: +86-400-840-9234', 'comments': 'Antiy Labs (Chine) – éditeur de moteurs antivirus (antivirus mobile AVL).' },
            { 'name': 'Apex', 'contact': 'Trend Micro, Inc. (USA) – 225 E John Carpenter Fwy, Irving, TX; +1-817-569-8900', 'comments': 'Trend Micro (USA) – solution corporate Apex One.' },
            { 'name': 'Arcabit', 'contact': 'Arcabit Sp. z o.o. (Pologne) – ul. Graniczna 50, 05-082 Blizne Łaszczyńskiego; +48-22-532-6900; biuro@arcabit.pl (ventes), pomoc@arcabit.pl (support)', 'comments': 'Arcabit (Pologne) – éditeur de l’antivirus Arcabit.' },
            { 'name': 'Avast', 'contact': 'Avast Software s.r.o. (CZ) – support global via le site (Anglais, multilingue); Twitter/FB disponibles', 'comments': 'Avast (République tchèque) – antivirus grand public et entreprise (maintenant Gen Digital).'},
            { 'name': 'Avast Mobile', 'contact': 'Voir Avast ci-dessus', 'comments': 'Avast Mobile Security (même société Avast).'},
            { 'name': 'AVG', 'contact': 'Gen Digital (ex-Avast) – USA: 2625 Broadway St, Redwood City, CA; CZ: Přízova 7, Brno', 'comments': 'AVG Technologies (Tchéquie, racheté par Avast) – antivirus grand public. '},
            { 'name': 'Avira', 'contact': 'Avira GmbH (Allemagne) – support portal (English)', 'comments': 'Avira (Allemagne) – éditeur de l’antivirus Avira (marque AntiVir).'},
            { 'name': 'AvWare', 'contact': 'BluePex Cybersecurity (Brésil) – appel gratuit 0800-520-6505', 'comments': 'Avware/BluePex (Brésil) – antivirus axé sur menaces latam:contentReference[oaicite:50]{index=50}.'},
            { 'name': 'Baidu', 'contact': 'Baidu, Inc. (USA) – 883 N Shoreline Blvd, Mountain View, CA; +1-669-224-6400; intlcomm@baidu.com', 'comments': 'Baidu (Chine) – géant Internet, fournit moteur anti-malware mobile.'},
            { 'name': 'Bitdefender', 'contact': 'Bitdefender SRL (Roumanie) – Șos. Orhideelor 15A, București; site support bitdefender.com', 'comments': 'Bitdefender (Roumanie) – éditeur renommé d’antivirus et de solutions de sécurité.'},
            { 'name': 'BitdefenderFalx', 'contact': 'Voir Bitdefender', 'comments': 'Bitdefender Falx (moteur de détection de Bitdefender).'},
            { 'name': 'BitdefenderTheta', 'contact': 'Voir Bitdefender', 'comments': 'Bitdefender Theta (moteur complémentaire de Bitdefender).'},
            { 'name': 'Bkav', 'contact': 'Bkav Corp. (Vietnam) – 2e étage, Bkav Bldg, Yen Hoa, Hanoi; +84-24-3763-2552; email Bkav@bkav.com', 'comments': 'Bkav (Vietnam) – éditeur de l’antivirus Bkav (accès locale).'},
            { 'name': 'Bkav Pro', 'contact': 'Voir Bkav ci-dessus', 'comments': 'Bkav Pro (Vietnam) – version entreprise de Bkav.'},
            { 'name': 'Cat_QuickHeal', 'contact': 'Quick Heal Ltd (Inde) – Solitaire Business Hub, Pune; +91-20-6681-3232; info@quickheal.com', 'comments': 'Cat QuickHeal (India) – ancien nom de Quick Heal, solutions endpoint et consumer.'},
            { 'name': 'ClamAV', 'contact': 'Project ClamAV (mailing-lists, forums); site cisco.com for source', 'comments': 'ClamAV – antivirus open-source pour email et fichiers (Cisco).'},
            { 'name': 'CMC', 'contact': 'CMC CyberSecurity (Vietnam) – siège: 15F, CMC Bldg, No.11 Duy Tan, Hanoi', 'comments': 'CMC (Vietnam) – éditeur d\'antivirus (menaces Asia).'},
            { 'name': 'CommTouch', 'contact': 'Cyren, Inc. (USA/Israël) – Data443 Corp, 155 Orchard Dr, STE 300, Gaithersburg, MD', 'comments': 'Cyren (ex-Commtouch, USA) – sécurité Internet cloud (emails, web).'},
            { 'name': 'Comodo', 'contact': 'Sectigo (anciennement Comodo CA) – support via portal Sectigo', 'comments': 'Sectigo/Comodo – éditeur de certificats SSL et aussi de solutions antivirus.'},
            { 'name': 'CrowdStrike', 'contact': 'CrowdStrike, Inc. (USA) – support via www.crowdstrike.com', 'comments': 'CrowdStrike (USA) – plateforme EDR et intelligence menaces.'},
            { 'name': 'CTX', 'contact': 'CTX Technology (USA) – email support@ctxtec.com; tel +1-877-688-3288', 'comments': 'CTX (USA) – solutions IT et sécurité (ex-VIPRE).'},
            { 'name': 'Cybereason', 'contact': 'Cybereason, Inc. (Israel) – support via portal \'The Nest\'; Tel-Aviv: Yigal Alon 94, Floor 37', 'comments': 'Cybereason (USA/Israël) – plateforme de détection/réponse (EDR) avancée.'},
            { 'name': 'Cylance', 'contact': 'BlackBerry Cylance – 2200 University Ave E, Waterloo, ON', 'comments': 'Cylance (USA/Canada) – antivirus par IA (acquis par BlackBerry).'},
            { 'name': 'Cynet', 'contact': 'Cynet Ltd – USA: 33 Arch St, Boston, MA 02110 +1-857-302-1237; ISR: Derech Menachem Begin 132, Tel-Aviv +972-3-376-9940', 'comments': 'Cynet (Israël/USA) – plateforme de sécurité (EDR).'},
            { 'name': 'Cyren', 'contact': 'Data443 (RansonMD, USA) – Cyren brand', 'comments': 'Cyren (USA/Israël) – sécurité email/web (ancien Commtouch).'},
            { 'name': 'DeepInstinct', 'contact': 'Deep Instinct, Inc. (USA) – 888 7th Ave, 5th Fl, New York, NY 10106; +1-347-534-1315', 'comments': 'Deep Instinct (USA/Israël) – solutions Deep Learning pour la sécurité des endpoints.'},
            { 'name': 'DrWeb', 'contact': 'Doctor Web (Russie) – FR: 333b Av. de Colmar, Strasbourg; +33-3-90-40-40-20', 'comments': 'Doctor Web (Russie) – éditeur de Dr.Web antivirus (global).'},
            { 'name': 'eGambit', 'contact': 'TEHTRIS SARL (France) – tel +33-1-88-33-53-33; email business@tehtris.com', 'comments': 'eGambit (France) – solution sécurité réseau de Tehtris.'},
            { 'name': 'Elastic', 'contact': 'Elastic NV (Pays-Bas) – siège: Keizersgracht 281, 1016 ED Amsterdam', 'comments': 'Elastic (Pays-Bas/USA) – éditeur d’Elasticsearch et de la suite Elastic Security.'},
            { 'name': 'Emsisoft', 'contact': 'Emsisoft Ltd (NZ) – 315a Hardy St, Nelson 7010, NZ', 'comments': 'Emsisoft (NZ) – antivirus et anti-malware (Grand public/Entreprise).'},
            { 'name': 'Endgame', 'contact': 'Endgame, Inc. (USA) – 3101 Wilson Blvd #500, Arlington, VA; +1-703-653-0361; info@endgame.com', 'comments': 'Endgame (USA) – endpoint protection (acquis par Elastic).'},
            { 'name': 'eScan', 'contact': 'MicroWorld Software (Inde) – support via site global; +91-22-6772-2911; emails support@escanav.com', 'comments': 'eScan (Inde) – antivirus grand public et entreprises.'},
            { 'name': 'ESET', 'contact': 'ESET, spol. s r.o. (Slovaquie) – Aupark Tower, Einsteinova 24, Bratislava; +421-2-322-44111; USA: 610 W Ash St, San Diego, CA', 'comments': 'ESET (Slovaquie) – éditeur du NOD32 Antivirus; solution entreprise/Home.'},
            { 'name': 'F-Prot', 'contact': 'FRISK Software (Islande) – intégré à Cyren', 'comments': 'F-Prot (Islande) – ancien antivirus FRISK (acquis par Commtouch/Cyren).'},
            { 'name': 'F-Secure', 'contact': 'F-Secure Corporation (Finlande) – Tammasaarenkatu 7, 00180 Helsinki; +358-9-2520-0100', 'comments': 'F-Secure (Finlande) – solutions antivirus et sécurité (safe banking, etc.).'},
            { 'name': 'FireEye', 'contact': 'Voir Mandiant (USA) – Sales: +1-877-666-1502', 'comments': 'FireEye (USA) – devenu Mandiant/Google Cloud; renseignement et réponse cyber.'},
            { 'name': 'Fortinet', 'contact': 'Fortinet, Inc. (USA) – 909 Kifer Rd, Sunnyvale, CA 94086; sales: +1-866-868-3678', 'comments': 'Fortinet (USA) – éditeur de pare-feux FortiGate et solutions réseau.'},
            { 'name': 'GData', 'contact': 'G DATA Software, Inc. (USA) – 200 Continental Dr, Ste 401, Newark, DE 19713; email presse@remove-this.gdata.de', 'comments': 'G DATA (Allemagne) – antivirus grand public (Made in Germany).'},
            { 'name': 'Google', 'contact': 'Google LLC (USA) – 1600 Amphitheatre Pkwy, Mountain View, CA; presse: press@google.com', 'comments': 'Google (USA) – moteur Safe Browsing; support via support.google.com.'},
            { 'name': 'Gridinsoft', 'contact': 'Gridinsoft LLC (Ukraine) – Lesya Kurbasa Ave 7B, 03194 Kyiv; +38-044-405-8232; support@gridinsoft.com', 'comments': 'Gridinsoft (Ukraine) – éditeur du Gridin Antivirus (malware hunter).'},
            { 'name': 'Huorong', 'contact': 'Huorong (Chine) – affilié au groupe Rising (Qihoo 360)', 'comments': 'Huorong (Chine) – moteur antivirus mobile de Rising/360.'},
            { 'name': 'Ikarus', 'contact': 'IKARUS Security Software GmbH (Autriche) – Blechturmgasse 11, 1050 Vienna; +43-1-58995-0; office@ikarus.at:contentReference[oaicite:129]{index=129}', 'comments': 'IKARUS Security (Autriche) – éditeur de solutions anti-malware (OT/IT):contentReference[oaicite:130]{index=130}.'},
            { 'name': 'Invincea', 'contact': 'Sophos (après acquisition) – contacter Sophos via sophos.com', 'comments': 'Invincea (USA) – moteur heuristique avancé (maintenant Sophos).'},
            { 'name': 'Jiangmin', 'contact': 'Jiangmin (Chine) – voir site Jiangmin Security', 'comments': 'Jiangmin (Chine) – ancien éditeur d’antivirus, peu d’infos publiques.'},
            { 'name': 'K7Antivirus', 'contact': 'K7 Computing (Inde/SG) – support Inde: 1800-419-0077; USA: +1-302-440-1497; emails sales/support sur k7computing.com', 'comments': 'K7 Computing (Inde) – éditeur d’anti-virus InfiniShield/K7, support global.'},
            { 'name': 'K7Gw', 'contact': 'Voir K7Antivirus', 'comments': 'K7Gw (K7 Global) – version en ligne/cloud du moteur K7.'},
            { 'name': 'Kaspersky', 'contact': 'Kaspersky Lab GmbH (Allemagne) – Schloßlände 26, 85049 Ingolstadt; +49-841-981890; info@kaspersky.de', 'comments': 'Kaspersky Lab (Russie/Allemagne) – éditeur de l’Anti-Virus Kaspersky.'},
            { 'name': 'Kingsoft', 'contact': 'Kingsoft Corp. (Chine) – 33 Xiaoying W Rd, Haidian, Beijing', 'comments': 'Kingsoft (Chine) – éditeur de WPS Office et Kingsoft Internet Security.'},
            { 'name': 'Lionic', 'contact': 'Lionic Corp (Taïwan) – 1F-C6, No.1 Lising 1st Rd., Hsinchu 30078; sales@lionic.com; +886-3-5789399', 'comments': 'Lionic Corp (Taïwan) – DPI & IoT security (AegisLab lab interne).'},
            { 'name': 'Malwarebytes', 'contact': 'Malwarebytes, Inc. (USA) – support@malwarebytes.com; +1-800-520-2796:contentReference[oaicite:145]{index=145}', 'comments': 'Malwarebytes (USA) – éditeur du Malwarebytes Anti-Malware:contentReference[oaicite:146]{index=146}.'},
            { 'name': 'Max', 'contact': 'Max Secure Software (Inde) – formulaire contact en ligne (maxpcsecure.com)', 'comments': 'Max Secure (Inde) – antivirus domestique (site en anglais/hindi).'},
            { 'name': 'MaxSecure', 'contact': 'Voir Max ci-dessus', 'comments': 'Max Secure (Inde) – même éditeur que Max.'},
            { 'name': 'McAfee', 'contact': 'McAfee, LLC (USA) – 6220 America Center Dr, San Jose, CA 95002; support via service.mcafee.com', 'comments': 'McAfee (USA) – anciennement Intel Security, éditeur de solutions endpoint et réseau.'},
            { 'name': 'McAfee_GW_Edition', 'contact': 'Voir McAfee ci-dessus', 'comments': 'McAfee Gateway (McAfee GW Edition) – version réseau de McAfee.'},
            { 'name': 'Microsoft', 'contact': 'Microsoft Corp (USA) – siège Redmond, WA; support via support.microsoft.com', 'comments': 'Microsoft (USA) – éditeur de Windows Defender/Defender ATP.'},
            { 'name': 'Microworld_eScan', 'contact': 'Voir eScan ci-dessus', 'comments': 'eScan (MicroWorld, Inde) – moteur antivirus.'},
            { 'name': 'NANO', 'contact': 'NANO Security Ltd (Russie) – Tel: +7-905-103-0737; e-mail: company@nanoav.ru', 'comments': 'NANO (Russie) – éditeur du NANO Antivirus.'},
            { 'name': 'Norton', 'contact': 'NortonLifeLock Inc. (USA) – 60 E Rio Salado Pkwy, Tempe, AZ; support via support.norton.com', 'comments': 'Norton (USA) – antivirus grand public (ex-Symantec Consumer).'},
            { 'name': 'NProtect', 'contact': 'AhnLab (Corée) – même adresse que AhnLab', 'comments': 'AhnLab nProtect (Corée) – sécurité réseau/applications.'},
            { 'name': 'Paloalto', 'contact': 'Palo Alto Networks (USA) – support via paloaltonetworks.com', 'comments': 'Palo Alto Networks (USA) – next-gen firewalls, Cortex XDR.'},
            { 'name': 'Panda', 'contact': 'Panda Security (Espagne) – site panda.com/contact (support via formulaire)', 'comments': 'Panda (Espagne) – éditeur de solutions antivirus/endpoint globales.'},
            { 'name': 'Prevx1', 'contact': 'Webroot, Inc. (USA) – support via webroot.com', 'comments': 'Prevx (Royaume-Uni) – moteur antimalware racheté par Webroot.'},
            { 'name': 'Qihoo_360', 'contact': 'Qihoo 360 (Chine) – site 360.cn; plus bureaux Beijing', 'comments': 'Qihoo 360 (Chine) – éditeur de 360 Total Security (mobile + PC).'},
            { 'name': 'Rising', 'contact': 'Rising (Chine) – affilié Qihoo, contact via 360.cn', 'comments': 'Rising (Chine) – ancien éditeur, maintenant moteur sous 360.'},
            { 'name': 'Sangfor', 'contact': 'Sangfor Technologies (Chine) – site sangfor.com', 'comments': 'Sangfor (Chine) – solutions sécurité et firewall.'},
            { 'name': 'SentinelOne', 'contact': 'SentinelOne, Inc. (USA) – support via sentinelone.com', 'comments': 'SentinelOne (USA) – plateforme XDR/EDR IA.'},
            { 'name': 'Sophos', 'contact': 'Sophos Ltd (UK) – 1 Kingdom St, London; support via sophos.com', 'comments': 'Sophos (UK) – antivirus et solutions réseau.'},
            { 'name': 'Sunbelt', 'contact': 'GFI Software (USA) – support via vipreantivirus.com', 'comments': 'Sunbelt Software (USA) – créateur de Vipre (maintenant GFI).'},
            { 'name': 'Superantispyware', 'contact': 'SuperAntiSpyware (USA) – support via superantispyware.com', 'comments': 'SuperAntiSpyware (USA) – outils anti-spyware gratuits.'},
            { 'name': 'Symantec', 'contact': 'NortonLifeLock (USA) – 60 E Rio Salado Pkwy, Tempe, AZ; contact support.norton.com', 'comments': 'Symantec (USA) – ancien éditeur de Norton AV.'},
            { 'name': 'SymantecMobileInsight', 'contact': 'NortonLifeLock (USA) – mêmes coordonnées que Norton/Symantec', 'comments': 'Symantec Mobile Insight – ancien moteur SmartProtection (Symantec).'},
            { 'name': 'Tachyon', 'contact': 'McAfee (USA) – 6220 America Center Dr, San Jose, CA', 'comments': 'TACHYON (McAfee) – moteur heuristique Nx sans signature.'},
            { 'name': 'Tencent', 'contact': 'Tencent (Chine) – siège Shenzhen, support via wechat/tencent.com', 'comments': 'Tencent (Chine) – éditeur PCManager (moteur antivirus WeSafe).'},
            { 'name': 'TheHacker', 'contact': 'Unknown', 'comments': 'TheHacker – alias rare (moteur inconnu).'},
            { 'name': 'TotalDefense', 'contact': 'Total Defense (USA) – ancien CA/Sygate; support via totaldefense.com', 'comments': 'Total Defense (USA) – antivirus grand public (devenu CA Antiv. Security).'},
            { 'name': 'Trapmine', 'contact': 'Trapmine (USA) – Startup rachetée par VMware', 'comments': 'TrapMine (USA) – moteur EDR (acquis par VMware).'},
            { 'name': 'TrendMicro', 'contact': 'Trend Micro Inc. (USA) – 10101 N De Anza Blvd, Cupertino, CA; support global via trendmicro.com', 'comments': 'Trend Micro (Japon/USA) – éditeur de solutions antivirus (OfficeScan, Apex, etc.)'},
            { 'name': 'TrendMicro_HouseCall', 'contact': 'Trend Micro (USA) – HouseCall en ligne', 'comments': 'Trend Micro HouseCall – scanner antivirus en ligne gratuit.'},
            { 'name': 'Trustlook', 'contact': 'Trustlook (Chine/USA) – support via trustlook.com', 'comments': 'Trustlook (Chine) – mobile threat intelligence.'},
            { 'name': 'Varist', 'contact': 'Varist (USA) – support via varist.com', 'comments': 'Varist (USA) – éditeur de ScannerONE (cloud AV).'},
            { 'name': 'VBA32', 'contact': 'VirusBlokAda (Ukraine) – support via vba32.com', 'comments': 'VirusBlokAda (Ukraine) – éditeur de VBA32 Antivirus.'},
            { 'name': 'VIPRE', 'contact': 'VIPRE (USA) – support via vipreantivirus.com', 'comments': 'VIPRE (USA) – antivirus d\'entreprise (ex-Sunbelt).'},
            { 'name': 'Virit', 'contact': 'VIRIT (Russie) – support via verereg.ru', 'comments': 'VIRIT (Russie) – ancien moteur anti-virus VIREX.'},
            { 'name': 'Virobot', 'contact': 'ViRobot (Chine) – support via 360.cn', 'comments': 'ViRobot (Chine) – ancien moteur Rising/360.'},
            { 'name': 'Webroot', 'contact': 'Webroot, Inc. (USA) – 385 Interlocken Crescent, Broomfield, CO; support via webroot.com', 'comments': 'Webroot (USA) – antivirus en cloud (SecureAnywhere).'},
            { 'name': 'WhiteArmor', 'contact': '360 (Chine) – affilié Qihoo 360', 'comments': 'WhiteArmor (Chine) – moteur de détection réseau (360).'},
            { 'name': 'Yandex', 'contact': 'Yandex (Russie) – support via yandex.com', 'comments': 'Yandex (Russie) – Safe Browsing/moteur antivirus dans Yandex Browser.'},
            { 'name': 'Zillya', 'contact': 'Zillya! LLC (Ukraine) – support via zillya.com', 'comments': 'Zillya! (Ukraine) – antivirus gratuit local.'},
            { 'name': 'ZoneAlarm', 'contact': 'Check Point Software (USA) – 800 Bridge Pkwy, Redwood Shores, CA; support via checkpoint.com', 'comments': 'ZoneAlarm (Check Point, USA/Israël) – antivirus et pare-feu client.'},
            { 'name': 'Zoner', 'contact': 'Zoner Ltd (CZ) – support via zonersoft.com', 'comments': 'Zoner Antivirus (Tchéquie) – ancien produit (abandonné).'}
        ]
        for v in vendors:
            AVVendor.objects.get_or_create(name=v['name'], defaults={'contact': v['contact'], 'comments': v['comments']})
