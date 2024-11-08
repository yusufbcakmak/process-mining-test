

# 2. Gerekli Kütüphaneleri İçe Aktarın
import pandas as pd
import pm4py

# 3. Veri Setini Yükleyin
# Örnek bir CSV dosyasını yükleyelim
df = pd.read_csv('windows_event_log.csv')

# 4. Veri Setini İşleyin
# Tarih formatlarını dönüştürme
df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])

# 5. Event Log'u Oluşturun
event_log = pm4py.format_dataframe(df, case_id='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')

# 6. Process Modelini Oluşturun
net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(event_log)

# 7. Process Modelini Görselleştirin
pm4py.view_petri_net(net, initial_marking, final_marking)

# 8. Performans Analizi Yapın
# Throughput time hesaplama
throughput_times = pm4py.get_throughput_time(event_log)
print(throughput_times)