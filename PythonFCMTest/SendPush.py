import FCMManager as fcm

tokens = ["dY-f_WAfQ8erWRA1ZgnKTd:APA91bGUfgvDrmeBn_7vpu0aaOpLuHIngk-1c8JygoIjnvix9fbKTm3yp99T9zL1i-vfTSp"
          "-7Zv69pZokrdtpBswD1AKNUKcc_mqvemVY_ItC-WffgzWRfyMoMjbOSG6KSy7_Bui93a3"]
fcm.sendPush("Hi", "This is my next msg", tokens)
