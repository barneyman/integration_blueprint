import json

ce = open("/config/.storage/core.config_entries", encoding="utf8")
config_entries = json.load(ce)
ce.close()

de = open("/config/.storage/core.device_registry", encoding="utf8")
device_registry = json.load(de)
de.close()

ee = open("/config/.storage/core.entity_registry", encoding="utf8")
entity_registry = json.load(ee)
ee.close()

# find the id
for config_entry in config_entries["data"]["entries"]:
    if config_entry["domain"] == "barneyman":
        config_entry_id = config_entry["entry_id"]

        # https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
        # search devices
        newDevices = [
            device
            for device in device_registry["data"]["devices"]
            if device["config_entries"][0] != config_entry_id
        ]
        newEntities = [
            entity
            for entity in entity_registry["data"]["entities"]
            if entity["config_entry_id"] != config_entry_id
        ]
        newEntries = [
            entry
            for entry in config_entries["data"]["entries"]
            if entry["entry_id"] != config_entry_id
        ]

        device_registry["data"]["devices"] = newDevices
        entity_registry["data"]["entities"] = newEntities
        config_entries["data"]["entries"] = newEntries

        with open("/config/.storage/core.config_entries", "w", encoding="utf8") as f:
            json.dump(config_entries, f, indent=4)

        with open("/config/.storage/core.device_registry", "w", encoding="utf8") as f:
            json.dump(device_registry, f, indent=4)

        with open("/config/.storage/core.entity_registry", "w", encoding="utf8") as f:
            json.dump(entity_registry, f, indent=4)

        break
