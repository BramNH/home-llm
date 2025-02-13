# StableLM 2 Zephyr 1.6B
## rev1
- 1 epoch
- 2048 train ctx
- batch size 8
- learning rate 1e-5
- weight decay 0.1
- gradient clipping 1.0
- dataset size: small
+ it honestly works not terribly and I was kinda able to get it to respond to german
+ evaluation results: 0.7108953613807982

## rev2
- dataset size: large (also rewrote how it works slightly)
+ evaluation results: 
  - 600: 0.7826321467098166
  - 800: 0.8090614886731392
  - 1000: 0.7669902912621359
  - 1200: 0.7944983818770227
  - 1400: 0.8176914778856527
  - 1600: 0.8268608414239482
  - 1800: 0.8263214670981661
  - Final: 0.8274002157497303

# StableLM Zephyr 3B
## rev1
- 1 epoch
- 2048 train ctx
- batch size 8
- learning rate 1e-5
- weight decay 0.1
- gradient clipping 1.0
- lora rank: 32, alpha: 64
- accidentally forgot to turn off fine tuning of embeddings
- dataset size: large
+ evaluation results:
  - 400: 0.8344
  - 800: 0.9228694714131608
  - 1200: 0.9401294498381877
  - 1600: 0.95361380798274
  - Final (1929): 0.9492988133764833

# rev2
- not fine-tuning the embeddings (no added tokens)
- dataset: new version with varied system prompts/responses (small)
+ evauluation results:
  - 400: 0.6748893105629349
  - 800: 0.7280202403542062
  - 1200: 0.7685009487666035
  - 1600: 0.7798861480075902
  - Final (1967): 0.7849462365591398
+ definitely needs more data

# rev3
- lora rank: 64, alpha: 128
- dataset size: large 
+ evaluation results:
  - 400: 0.8785578747628083
  - 800: 0.9247311827956989
  - 1200: 0.9348513598987982
  - 1600: 0.9222011385199241
  - 2000: 0.9354838709677419
  - 2400: 0.9740670461733081
  - 2800: 0.9595192915876027
  - 3200: 0.948134092346616
  - 3600: 0.963314358001265
  - 4000: 0.9614168247944339
  - Final (~4200): 0.9538266919671095

# rev4
- lora rank: 64, alpha: 128
- dataset size: large (with new device types)
+ evaluation results:
  - 400: 0.867914979757085
  - 800: 0.9316801619433198
  - 1200: 0.9215587044534413
  - 1600: 0.9686234817813765
  - 2000: 0.9772267206477733
  - 2400: 0.9752024291497976  
  - 2800: 0.9802631578947368
  - 3200: 0.9777327935222672
  - 3600: 0.9812753036437247
  - 4000: 0.979251012145749
  - 4400: 0.978744939271255
  - 4800: 0.9777327935222672
  - Final (5234): 0.9782388663967612
+ overfit

# rev5
- lora rank: 64, alpha: 128
- dataset size: medium (with new device types)
+ evaluation results:
  - 400: 0.8709514170040485
  - 800: 0.9316801619433198
  - 1200: 0.9544534412955465
  - 1600: 0.9559716599190283
  - 2000: 0.9671052631578947
  - 2400: 0.9671052631578947
  - 2800: 0.9701417004048583
  - 3200: 0.9696356275303644
  - 3600: 0.9736842105263158
  - 4000: 0.9706477732793523
  - Final: 0.9711538461538461
