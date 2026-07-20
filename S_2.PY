import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import re

def dophina_engine_11_etapes(url, annees_simulees=3):
    print(f"\n" + "="*60)
    print(f" 🐬 DOPHINA 2.0 - MOTEUR D'AUDIT SÉCURISÉ & PASSIF")
    print("="*60)
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=60)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        score_exposition = 0
        server_headers = response.headers
        
        # ============================================================
        # [ÉTAPPE 1] à [ÉTAPPE 4] (Ton code d'origine intact)
        # ============================================================
        print("\n[ÉTAPPE 1] - FLUX D'ENVOI ET EN-TETES")
        print("-" * 50)
        hsts = server_headers.get('Strict-Transport-Security')
        if not hsts: 
            score_exposition += 20
            print("[ALERTE] Pas de configuration HSTS détectée.")
        else:
            print("[OK] Le serveur force le HTTPS strict.")
        serveur_brut = server_headers.get('Server', 'Inconnu')
        print(f"[Info] Signature du serveur : {serveur_brut}")

        print("\n[ÉTAPPE 2] - CARTOGRAPHIE DES RISQUES HTML")
        print("-" * 50)
        formulaires = soup.find_all('form')
        print(f" -> {len(formulaires)} formulaire(s) détecté(s).")
        for i, form in enumerate(formulaires, 1):
            if form.get('method', 'get').lower() == 'get': score_exposition += 15

        print("\n[ÉTAPPE 3] - ANALYSE DES SYSTEMES DE DÉFENSE")
        print("-" * 50)
        full_text_lower = str(server_headers).lower() + str(response.cookies).lower()
        bouclier = "Aucun"
        for waf in ['cloudflare', 'akamai', 'sucuri', 'wordfence']:
            if waf in full_text_lower: bouclier = waf.upper()
        print(f"[DÉTECTION] Bouclier de protection : {bouclier}")

        print("\n[ÉTAPPE 4] - L'USURE DU TEMPS & DÉTECTION DES ANOMALIES (+3 ANS)")
        print("-" * 50)
        commentaires = soup.find_all(string=lambda text: isinstance(text, type(BeautifulSoup().string)) and isinstance(text, str))
        mysteres_trouves = 0
        mots_anormaux = ['todo', 'fixme', 'test', 'admin', 'password', 'carlos']
        for com in commentaires:
            if any(mot in com.lower() for mot in mots_anormaux): mysteres_trouves += 1
        
        probabilite_rupture = min((mysteres_trouves * 15) + score_exposition + (annees_simulees * 8), 99.9)
        print(f"* Projections logiques pour l'année {2026 + annees_simulees} :")
        print(f"  -> Nombre d'anomalies/mystères accumulés : {mysteres_trouves}")
        print(f"  -> Probabilité de faille critique due à l'usure du temps : {probabilite_rupture}%")

        # ============================================================
        # [ÉTAPPE 5] - ANALYSE DES INCOHÉRENCES LOGIQUES & HORS NORMES
        # ============================================================
        print("\n[ÉTAPPE 5] - ANALYSE DES INCOHÉRENCES LOGIQUES (HORS NORMES)")
        print("-" * 50)
        incoherences = []
        
        if url.startswith("http://") and hsts:
            incoherences.append("Incohérence : Le site est appelé en HTTP clair mais prétend forcer le HSTS.")
            
        if not soup.find("meta", charset=True) and not soup.find("meta", attrs={"http-equiv": re.compile(r"content-type", re.I)}):
            incoherences.append("Hors norme : Aucune déclaration d'encodage de caractères (Risque de texte mal affiché).")
            
        set_cookie = server_headers.get('Set-Cookie', '')
        if set_cookie and "httponly" not in set_cookie.lower():
            incoherences.append("Anomalie : Des cookies sont transmis sans l'attribut de sécurité HttpOnly.")

        if incoherences:
            for inc in incoherences:
                print(f"  -> [ANOMALIE LOGIQUE] {inc}")
                score_exposition += 10
        else:
            print("  -> Structure logique et normes standards respectées par le serveur.")

        # ============================================================
        # [ÉTAPPE 7] - INVESTIGATION DES COULISSES (ROBOTS.TXT)
        # ============================================================
        print("\n[ÉTAPPE 7] - INVESTIGATION DES COULISSES NUMÉRIQUES")
        print("-" * 50)
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = urljoin(base_url, "/robots.txt")
        dossiers_caches = 0
        
        try:
            r_robots = requests.get(robots_url, headers=headers, timeout=5)
            if r_robots.status_code == 200:
                lignes = r_robots.text.split('\n')
                interdits = [l for l in lignes if "disallow" in l.lower()]
                dossiers_caches = len(interdits)
                print(f"[DÉTECTION] Fichier robots.txt trouvé ! ({dossiers_caches} dossiers masqués)")
                for p in interdits[:3]:
                    print(f"     [Dossier Caché] {p.strip()}")
            else:
                print(f"  -> Pas de fichier robots.txt accessible (Code : {r_robots.status_code})")
        except Exception:
            print("  -> Impossible d'interroger le fichier robots.txt (Timeout/Bloqué)")

        # ============================================================
        # [ÉTAPPE 8] - AUDIT DES EN-TÊTES DE SÉCURITÉ MANQUANTS
        # ============================================================
        print("\n[ÉTAPPE 8] - AUDIT DES PILIERS DE SÉCURITÉ (HEADERS)")
        print("-" * 50)
        headers_manquants = []
        piliers = {
            'X-Frame-Options': 'Protection contre le Clickjacking (Détournement de clic)',
            'X-Content-Type-Options': 'Protection contre le Sniffing de scripts Mime',
            'Content-Security-Policy': 'Contrôle des sources d\'exécution de scripts (Anti-XSS)'
        }
        for head, desc in piliers.items():
            if head not in server_headers:
                headers_manquants.append(head)
                print(f"  [MANQUE] {head} -> {desc}")
                score_exposition += 8
            else:
                print(f"  [OK] {head} est présent.")

        # ============================================================
        # [ÉTAPPE 9] - CARTOGRAPHIE DES TECHNOLOGIES VISIBLES
        # ============================================================
        print("\n[ÉTAPPE 9] - CARTOGRAPHIE DES DEPENDANCES VISIBLES")
        print("-" * 50)
        scripts = soup.find_all('script', src=True)
        css = soup.find_all('link', rel=re.compile(r'stylesheet', re.I))
        print(f"  -> {len(scripts)} script(s) externe(s) injecté(s) dans le HTML.")
        print(f"  -> {len(css)} fichier(s) de style CSS détecté(s).")
        
        techs_trouvees = []
        src_total = str(soup).lower()
        if 'jquery' in src_total: techs_trouvees.append('jQuery')
        if 'wordpress' in src_total: techs_trouvees.append('WordPress')
        if 'react' in src_total: techs_trouvees.append('React.js')
        
        if techs_trouvees:
            print(f"  [TECH DEHORS] Outils repérés : {', '.join(techs_trouvees)}")

        # ============================================================
        # [ÉTAPPE 11] - BLINDAGE AUTOMATIQUE & CONSEILS UTILISATEUR
        # ============================================================
        print("\n[ÉTAPPE 11] - RECOMMANDATIONS DE BLINDAGE PASSIF")
        print("-" * 50)
        conseils_solutions = []
        
        if not hsts:
            conseils_solutions.append("[CONSEIL HSTS] Ajoutez l'en-tête suivant sur votre serveur pour forcer le HTTPS : 'Strict-Transport-Security: max-age=63072000; includeSubDomains; preload'")
        if 'X-Frame-Options' in headers_manquants:
            conseils_solutions.append("[CONSEIL CLICKJACKING] Ajoutez l'en-tête de sécurité : 'X-Frame-Options: SAMEORIGIN'")
        if 'X-Content-Type-Options' in headers_manquants:
            conseils_solutions.append("[CONSEIL SNIFFING] Activez l'en-tête de blocage : 'X-Content-Type-Options: nosniff'")
        if 'Content-Security-Policy' in headers_manquants:
            conseils_solutions.append("[CONSEIL ANTI-XSS] Mettez en place une règle CSP de base : 'Content-Security-Policy: default-src 'self''")
        if any("HttpOnly" in inc for inc in incoherences):
            conseils_solutions.append("[CONSEIL COOKIES] Configurez vos scripts de session pour inclure le flag 'HttpOnly' et 'Secure' sur chaque cookie généré.")

        if conseils_solutions:
            print(f"  -> {len(conseils_solutions)} solution(s) de blindage générée(s) pour l'utilisateur.")
        else:
            print("  -> Aucun correctif requis, le site applique déjà les meilleures normes.")

        # ============================================================
        # [ÉTAPPE 6 & 10] - RAPPORT GLOBAL ENRICHI DOPHINA 2.0
        # ============================================================
        print("\n[ÉTAPPE 6 & 10] - COMPILATION DU RAPPORT")
        print("-" * 50)
        
        nom_fichier = "rapport_audit.txt"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(f"=================================================\n")
            f.write(f" 🐬       DOPHINA 2.0 - RAPPORT D'AUDIT PRO      \n")
            f.write(f"=================================================\n")
            f.write(f"Cible analysée : {url}\n")
            f.write(f"Signature Serveur : {serveur_brut}\n")
            f.write(f"Protection active : {bouclier}\n")
            f.write(f"Nombre de formulaires : {len(formulaires)}\n")
            f.write(f"Incohérences logiques : {len(incoherences)}\n")
            f.write(f"Dossiers confidentiels (robots.txt) : {dossiers_caches}\n")
            f.write(f"En-têtes de sécurité manquants : {len(headers_manquants)} ({', '.join(headers_manquants) if headers_manquants else 'Aucun'})\n")
            f.write(f"Scripts et Styles détectés : {len(scripts)} JS / {len(css)} CSS\n")
            f.write(f"-------------------------------------------------\n")
            f.write(f"Projection {2026 + annees_simulees} - Risque de vieillissement : {probabilite_rupture}%\n")
            if probabilite_rupture > 50:
                f.write(f"Bilan : Code exposé à l'usure du temps. Blindage conseillé.\n")
            else:
                f.write(f"Bilan : Structure stable et propre face au temps.\n")
            f.write(f"-------------------------------------------------\n")
            f.write(f" SOLUTIONS DE BLINDAGE RECOMMANDÉES :\n")
            if conseils_solutions:
                for sol in conseils_solutions:
                    f.write(f" * {sol}\n")
            else:
                f.write(f" * Votre site suit déjà les règles de l'art ! Rien à faire.\n")
            f.write(f"=================================================\n")
            
        print(f"[OK] Moteur Dophina 2.0 exécuté avec succès.")
        print(f"[INFO] Le rapport avec solutions est prêt : {os.path.abspath(nom_fichier)}")
        print("\n" + "="*60)

    except Exception as e:
        print(f"Erreur globale : {e}")

# Lancement sur Space Jam
url_cible = "https://www.exemple.com"
dophina_engine_11_etapes(url_cible, annees_simulees=3)
