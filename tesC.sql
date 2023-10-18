SELECT DISTINCT notebook, bag, mobile phone
FROM ASSET;

---

SELECT 
    user_id,
    CASE 
        WHEN nama = 'wildan' THEN 'notebook, bag'
        WHEN nama = 'zaki' THEN 'notebook, bag, mobile phone'
        ELSE NULL -- Untuk nilai selain 'wildan' dan 'zaki'
    END AS asset
WHERE 
    nama IN ('wildan', 'zaki');

