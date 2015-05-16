# Find all the llamas born between January 1, 1995 and December 31, 1998.
# Fill in the 'where' clause in this query.

QUERY = '''
select name, birthdate from animals where (species = 'llama') and (birthdate >= '1995-01-01' and birthdate <= '1998-12-31')
'''

# List taxonomic order by their common name, sorted by how many animals are in the zoo

QUERY = '''
select ordernames.name, count(*) as num
  from animals, taxonomy, ordernames
  where animals.species = taxonomy.name
    and taxonomy.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc;
  '''
