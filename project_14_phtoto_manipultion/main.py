import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def detect_and_highlight_edges(input_path, outout_path, low_threshold = 60 , high_threshold = 150, edge_color = (0,255,0)):

    image = cv2.imread(input_path)
    if image is None:
        raise ValueError(f"Could not read image at {input_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray,(5,5),0)

    edges = cv2.Canny(blurred, low_threshold, high_threshold)

    edge_mask = np.zeros_like(image)

    edge_mask[edges != 0] = edge_color


    highlighted_edges = cv2.addWeighted(image,1 ,edge_mask,0.7,0)

    edges_only =np.ones_like(image) * 255
    edges_only[edges != 0] = edge_color

    combined = np.hstack((image,highlighted_edges,edges_only)) 

    cv2.imwrite(outout_path, combined)


    plt.figure(figsize=(15,5))
    plt.subplot(131), plt.imshow(cv2.cvtColor(image,cv2.COLOR_RGB2BGR)), plt.title('Original')
    plt.subplot(132), plt.imshow(cv2.cvtColor(highlighted_edges,cv2.COLOR_RGB2BGR)), plt.title('Highlighted Edges')
    plt.subplot(133), plt.imshow(cv2.cvtColor(edges_only, cv2.COLOR_RGB2BGR)),plt.title('Edges Only')
    plt.tight_layout()
    plt.show()

    print(f"Edge detection complete. Result saved to {outout_path}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect and highlight edges in an image')
    parser.add_argument('input',help='Path to the input image')
    parser.add_argument('output',help='Path to the output image')
    parser.add_argument('--low',type=int, default=50, help='Lower threshold for Canny edge detection')
    parser.add_argument('--high',type=int, default=150, help='Upper threshold for Canny edge detection')
    parser.add_argument('--color', nargs=3, type=int, default=[0,255,0], help='Color to highlight edges (B G R)')
    args = parser.parse_args()
    detect_and_highlight_edges(args.input,args.output,args.low,args.high,tuple(args.color))
