def big_line():
    print('-=' * 34)

big_line()
print('Max Pistol Stats, Resident Evil 4 Remake - Format Specifiers'.center(68).upper())
big_line()

pistols = [
    ('Blacktail', 2.40, 13, 1.60, '1.5 More Power'),
    ('SG-09 R', 2.0, 18, 1.40, '5x Critical Hit Rate'),
    ('Red 9', 2.70, 16, 1.25, '1.5 More Power'),
    ('Punisher', 1.90, 24, 1.50, '5x Penetration Power')
]

shotguns = [
    ('W-870', 10.1, 10, 0.95, '2x More Power'),
    ('Striker', 16.2, 24, 0.62, '2x Ammo Capacity'),
    ('Riot Gun', 12.8, 12, 0.97, '1.5x Power')
]

rifles = [
    ('SR M1903', 5.30, 13, 0.61, '2x More Power'),
    ('Stingray', 4.90, 18, 1.18, '2x Rate of Fire'),
    ('Assault Rifle', 4.60, 32, 1.25, '1.5x More Power')
]

print(f'| {'PISTOL':^10} | {'DAMAGE':^6} | {'AMMO':^3} | {'RELOAD SPEED':^10} | {'EXCLUSIVE':^20} |')

for pistol, damage, ammo, reload, exclusive in pistols:
    print(f'| {pistol:^10} | {damage:^6} | {ammo:^4} | {reload:^12} | {exclusive:^20} |')

big_line()
print('Max Shotgun Stats, Resident Evil 4 Remake - Format Specifiers'.center(72).upper())
big_line()

print(f'| {'SHOTGUN':^10} | {'DAMAGE':^6} | {'AMMO':^4} | {'RELOAD SPEED':^12} | {'EXCLUSIVE':^20} |')

for shotgun, dam, ammo_cap, reload_speed, exc in shotguns:
    print(f'| {shotgun:^10} | {dam:^6} | {ammo_cap:^4} | {reload_speed:^12} | {exc:^20} |')

big_line()
print('Max Rifle Stats, Resident Evil 4 Remake - Format Specifiers'.center(72).upper())
big_line()

print(f'| {'RIFLE':^15} | {'DAMAGE':^6} | {'AMMO':^4} | {'RELOAD SPEED':^12} | {'EXCLUSIVE':^15} |')

for rifle, d, a, rs, e in rifles:
    print(f'| {rifle:^15} | {d:^6} | {a:^4} | {rs:^12} | {e:^15} |')
big_line()