# 2. Gerekli Kütüphaneleri İçe Aktarın
import win32evtlog
import pandas as pd

# 3. Event Log'ları Okuyun
server = 'localhost'  # Yerel makine
log_type = 'System'  # Okunacak log türü (Application, Security, System vb.)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

# Event Log'ları toplamak için bir liste oluşturun
event_list = []

# Event Log'ları okuyun
handle = win32evtlog.OpenEventLog(server, log_type)
while True:
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    if not events:
        break
    for event in events:
        event_dict = {
            'EventID': event.EventID,
            'TimeGenerated': event.TimeGenerated,
            'SourceName': event.SourceName,
            'EventCategory': event.EventCategory,
            'EventType': event.EventType,
            'EventData': event.StringInserts
        }
        event_list.append(event_dict)

# 4. Verileri İşleyin ve Kaydedin
df = pd.DataFrame(event_list)
df['TimeGenerated'] = pd.to_datetime(df['TimeGenerated'])

# CSV dosyasına kaydedin
df.to_csv('windows_event_log.csv', index=False)

print("Event log'lar başarıyla toplandı ve windows_event_log.csv dosyasına kaydedildi.")