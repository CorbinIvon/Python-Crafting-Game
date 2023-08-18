import items
biomes = {
  'Grassland': {
    'description': 'A wide expanse of grassy plains.',
    'danger': 0,
    'resources': {
      items['Stick']: 1,
      items['rock']: 2,
      items['Plant Fiber']: 2,
      items['Berries']: 1,
      items['Water']: 1,
    }
  },
  'forest': {
    'description': 'A dense forest of trees.',
    'danger': 1,
    'resources': {
      items['Stick']: 8,
      items['Wood Log']: 2,
      items['rock']: 2,
      items['Plant Fiber']: 2,
      items['Berries']: 2,
      items['Water']: 2,
    }
  },
}
