from influxdb import InfluxDBClient
import matplotlib.pyplot as plt
import numpy as np

data_frame  = [#Alpha = 0.0
['4d036c2d-76e7-4995-94a6-863e88edb0ce',
'6866ed4f-990b-4b73-923a-1740e30c30a7',
'c6d34169-e1fe-4ca9-8033-a1de3d755c7b',
'cc072630-d8ce-43b2-9780-f6e5b4e9da4b',
'21941113-50b8-4996-8f5c-f4cfa9ed5933',
'64690845-0e86-44f1-9d8c-efb9eaa7c9b5',
],

#Alpha = 0.1
['8bad5e38-5d73-451a-a8e9-48c7e7348c11',
'87140e32-1488-4f43-89c0-679624d03ae5',
'a4e091c1-a513-4c67-8a64-7913c05b51b1',
'9dfb06d3-9ede-4e01-b77d-28348433dd49',
'e1262920-1a29-4c69-9f39-82323f3158b5',
'f50413c7-8490-4c32-9d13-9d5928417c16',
'd405e009-596e-4178-8a91-0541ba62bddd',
],

#Alpha = 0.2
['c69525f4-a3a4-446c-97b2-ddc1b6f1dfe6',
'f8587984-bddb-4228-bee6-07d27e077e41',
'ba1f07e4-617d-4758-9839-d33934440fd9',
'fb9cf9b2-e880-4594-bfb6-899fcd2ec3e1',
'4f9e0315-f272-42da-a08e-58a49b458a33',
],

#Alpha = 0.3
['b25a4e4c-6273-4016-a92d-8b2449f1ba86',
'bee09d36-8ab7-4063-a884-77fda0b556e8',
'5b6937f2-3459-44ba-80f3-5dde767ab047',
'c04c5082-0e71-4ead-b651-ee736fcbe3c0',
'506a520d-8e38-4f44-b964-3207b85df81e',
],

#Alpha = 0.4
['e7c69ff7-fbfc-4649-aaa6-cf9409a41836',
'5f87d8cb-ca86-4443-b196-64e55af481c4',
'e3781c01-41d4-444a-8117-145a39602b17',
'6f0161fe-2251-4ebc-a340-6e8b7ea6e544',
'e138362c-c111-48c6-9d71-31bfc9d6033d',
],

#Alpha = 0.5
['0c27f642-c918-4312-8bd9-669ed4e54b1b',
'7622d4bd-5e3d-4e05-84db-c411291a40f7',
'b989f635-9314-4005-853e-6c3073081b1c',
'5f189800-0c87-4ae9-ac2b-1cba83524617',
'ce1bf166-8a3e-4f72-97f4-e4e57ab88a1d',
],

#Alpha = 0.6
['fab40b36-e4a0-4083-aa4f-956718924475',
'b9faa828-8129-48bc-ba64-eb185e727043',
'ed70dd52-3e08-44b8-b565-6b16ee4df9c9',
'1fa2977b-b68b-4ec9-a4b5-9af82f3727f6',
'5d79b839-acb6-4b67-8aec-3b47cc02190b',
],


#Alpha = 0.7
['5eed9297-4ddb-4dd4-8212-bf18d7a3022e',
'c624885c-a711-4778-b763-81d5ea44184b',
'f5d88c78-c649-40a4-8161-dc2769930bab',
'8441cf0e-1b15-4b6c-ab4f-b317dcb6e780',
'26f314a0-d967-437a-abc7-b0554a218ca8',
],

#Alpha = 0.8

['f4097ab6-3935-40d4-8918-f3c1a5d4e87d',
'0753637f-dd56-47ed-a1f0-e8f4a4402fe9',
'a89c6c48-fd06-43a6-9794-5636e7e15070',
'6fb69f23-2856-4a3b-bf4d-d6f6db61becd',
'560b784f-5d2d-42bc-a299-c3e5af4c6306',
],

#Alpha = 0.9
['74a45166-a6c8-48e5-b8d8-5f7ebc13c1dc',
'5f3c5df0-6572-4b0e-a391-6d7243a982f9'
],

#Alpha = 1.0

]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'mdp')

#uuid = 'fb9cf9b2-e880-4594-bfb6-899fcd2ec3e1'

data = []



for i in range(len(data_frame)): #10
    data.append([])
    for j in range(len(data_frame[i])):
        uuid = data_frame[i][j]
        query = f"select tot_rwd from run where id='{uuid}'"
        response = client.query(query=query)
        test = response.raw
        total_trial_reward = list(np.asarray(test['series'][0]['values'])[:, 1])
        data[i].append(total_trial_reward)
    print('---')


