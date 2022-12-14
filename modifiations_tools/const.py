from pyrosetta.rosetta.core import chemical

NC_AAS_PATCH = {
    'ALY': {'cognateAA': 'LYS',
            'type': chemical.VariantType.ACETYLATION},
    'SCY': {'cognateAA': 'CYS',
            'type': chemical.VariantType.ACETYLATION},
    'TYI': {'cognateAA': 'TYR',
            'type': chemical.VariantType.DIIODINATION},
    'MLY': {'cognateAA': 'LYS',
            'type': chemical.VariantType.DIMETHYLATION},
    'CCX': {'cognateAA': 'GLU',
            'type': chemical.VariantType.CARBOXYLATION},
    'HYP': {'cognateAA': 'PRO',
            'type': chemical.VariantType.HYDROXYLATION1},
    'OAZ': {'cognateAA': 'PRO',
            'type': chemical.VariantType.HYDROXYLATION2},
    'HIC': {'cognateAA': 'HIS',
            'type': chemical.VariantType.METHYLATION},
    'MLZ': {'cognateAA': 'LYS',
            'type': chemical.VariantType.METHYLATION},
    'FME': {'cognateAA': 'MET',
            'type': chemical.VariantType.N_FORMYLATION},
    'SEP': {'cognateAA': 'SER',
            'type': chemical.VariantType.PHOSPHORYLATION},
    'TPO': {'cognateAA': 'THR',
            'type': chemical.VariantType.PHOSPHORYLATION},
    'PTR': {'cognateAA': 'TYR',
            'type': chemical.VariantType.PHOSPHORYLATION},
    'TYS': {'cognateAA': 'TYR',
            'type': chemical.VariantType.SULFATION},
    'M3L': {'cognateAA': 'LYS',
            'type': chemical.VariantType.TRIMETHYLATION},
}
