#!/usr/bin/python
import json
class FilterModule(object):
    'Filter output after self_heal response'
    def filters(self):
        'Define filters'
        return {
            'ovirtselfheal': self.ovirtselfheal
        }

    def ovirtselfheal(self, ovirt_heal_response):
        'Return 1 if heal is in progress else 0'
        return self._parse_self_heal_result(ovirt_heal_response)

    @staticmethod
    def _parse_self_heal_result(heals):
        flag = False
        if heals.get('ansible_facts') is not None:
            for heal in heals.get('ansible_facts').get('glusterfs').get('heal_info'):
                if heal.get('no_of_entries') is not None and heal.get('no_of_entries').isnumeric():
                    if int(heal.get('no_of_entries')) > 0:
                        flag = True
                        break;
        return flag
