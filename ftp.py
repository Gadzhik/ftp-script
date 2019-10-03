#!/usr/bin/python
import os
import ftplib


ftpsrv = ftplib.FTP('ftp.somehost.com')
ftpsrv.login()
ftpsrv.cwd('directory')
files = ftpsrv.nlst()

for file in files:
      remote_file = os.path.join(
            'D:\\some_folder', file
      )

      try:
            with open(remote_file, 'wb') as local_file:
                  ftpsrv.retrbinary('RETR ' + file, local_file.write)
      except ftplib.error_perm:
            pass

ftpsrv.quit()