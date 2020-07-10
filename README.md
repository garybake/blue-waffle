# blue-waffle
Source set of x type images to train a model and then find them for sale on ebay/fb  

If we want listings of measuring rulers and not monarcy rulers. We can search ebay/fb
for "rulers" and then use the trained model to discriminate and just show measuring rulers.

Generate training data
======================

Generate enough source images. i.e. if you wanted to train a model to differentiate swans from sausages.  

```bash
$ python get_images.py swan sausage
```