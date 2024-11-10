
def detect(image, detector):
        results = detector(image, verbose=False)
        
        if len(results[0]) != 0:
            prediction = {
            'x': int(results[0].to("cpu").numpy().boxes.xywh[:, 0][0]),
            'y': int(results[0].to("cpu").numpy().boxes.xywh[:, 1][0]),
            'w': int(results[0].to("cpu").numpy().boxes.xywh[:, 2][0]),
            'h': int(results[0].to("cpu").numpy().boxes.xywh[:, 3][0]),
            }
            prediction['confidence'] = str(results[0].to("cpu").numpy().boxes.conf[0])
            prediction['class'] = str((results[0].to("cpu").numpy().boxes.cls)[0].astype(int))

            return prediction
        else:
            #print(f"{type} not found!")
            return {
                'x': 0,
                'y': 0,
                'w': 0,
                'h': 0,
            }