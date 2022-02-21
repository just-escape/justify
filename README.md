```
pip3 install jinja2
```

```
% python3 vouchers.py <vouchers_file.csv> {1,2,3,4} <template_file.svg>

% python3 vouchers.py sample.csv 1 template.txt
Filling coupons_speciaux_0.svg
Filling coupons_speciaux_1.svg
Done

% python3 vouchers.py sample.csv 1 template.txt --n-codes-per-template 6 --output-file-basename coupons_speciaux
Filling coupons_speciaux_0.svg
Filling coupons_speciaux_1.svg
Filling coupons_speciaux_2.svg
Filling coupons_speciaux_3.svg
Done
```
