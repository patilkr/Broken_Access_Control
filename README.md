# OWASP Top 10 - Web Application Threats
-----------------------------------------------------------
## Broken_Access_Control
**OWASP-A5-2017 - Broken Access Control**
-----------------------------------------------------------
# Usage Examples:
### owaspBricksIDOR.py : - Insecure Direct Object Reference (IDOR) Scanner Tested with Bricks.
* python3 owaspBricksIDOR.py -s 0 -e 3 --url http://<i></i>ipAddress/owaspbricks/content-1/index.php?id=
  
### mutillidae_LFI.py: - Local File Inclusion (LFI) Vulnerability Tested with  Mutillidae.
* python3 mutillidae_LFI.py -f /etc/hosts  -u http://<i></i>example.com/index.php?page= 
* python3 mutillidae_LFI.py --url http://<i></i>example.com/index.php?page= 

### get_shell.php : - Remote File Inclusion (RFI) Vulnerability Exploitation Shell Code.
-----------------------------------------------------------

