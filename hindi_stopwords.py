

HINDI_STOPWORDS = [
    "aur",  # and
    "hai",  # is
    "hain",  # are
    "ho",  # are / be
    "hoon",  # am
    "ka",  # of (masculine singular)
    "ke",  # of (masculine plural / respectful)
    "ki",  # of (feminine) / that
    "ko",  # to / for
    "se",  # from / by / with
    "me",  # in / inside
    "par",  # on / at / but
    "tak",  # until / up to
    "ne",  # subject marker (past tense)
    "bhi",  # also / too
    "hi",  # only / emphasized
    "to",  # then / so
    "ya",  # or
    "lekin",  # but
    "parantu",  # but / however
    "magar",  # but
    "kya",  # what / question marker
    "kaun",  # who
    "kahan",  # where
    "kab",  # when
    "kyun",  # why
    "kaise",  # how (masculine plural / formal)
    "kaisi",  # how (feminine)
    "kaisa",  # how (masculine singular)
    "kitna",  # how much (masculine singular)
    "kitne",  # how many (masculine plural)
    "kitni",  # how much/many (feminine)
    "vah",  # he / she / it / that
    "ve",  # they / those
    "yah",  # this / it
    "ye",  # these / they
    "use",  # him / her / to that
    "isne",  # this person (subject)
    "usne",  # that person (subject)
    "inhoone",  # these people (subject)
    "unhoone",  # those people (subject)
    "isse",  # from this
    "usse",  # from that
    "ismein",  # in this
    "usmein",  # in that
    "iski",  # its / her / his (feminine)
    "iska",  # its / her / his (masculine singular)
    "iske",  # its / her / his (masculine plural)
    "uski",  # that person's (feminine)
    "uska",  # that person's (masculine singular)
    "uske",  # that person's (masculine plural)
    "unka",  # their / respectful his/her (masculine singular)
    "unke",  # their / respectful his/her (masculine plural)
    "unki",  # their / respectful his/her (feminine)
    "inka",  # these people's (masculine singular)
    "inke",  # these people's (masculine plural)
    "inki",  # these people's (feminine)
    "main",  # I
    "mera",  # my / mine (masculine singular)
    "mere",  # my / mine (masculine plural)
    "meri",  # my / mine (feminine)
    "mujhe",  # me / to me
    "mujhse",  # from me
    "tum",  # you (informal)
    "tumhara",  # your (masculine singular)
    "tumhare",  # your (masculine plural)
    "tumhari",  # your (feminine)
    "tumhe",  # you / to you
    "aap",  # you (formal/respectful)
    "aapka",  # your (formal, masculine singular)
    "aapke",  # your (formal, masculine plural)
    "aapki",  # your (formal, feminine)
    "aapko",  # to you (formal)
    "aapse",  # from you (formal)
    "hum",  # we / us
    "hamara",  # our (masculine singular)
    "hamare",  # our (masculine plural)
    "hamari",  # our (feminine)
    "humein",  # us / to us
    "humse",  # from us
    "apna",  # one's own (masculine singular)
    "apne",  # one's own (masculine plural)
    "apni",  # one's own (feminine)
    "aapas",  # each other / mutually
    "swayam",  # self / oneself
    "khud",  # self / by oneself
    "kuch",  # some / something
    "koi",  # someone / any
    "sab",  # all / everything
    "sabhi",  # everyone / all
    "dono",  # both
    "teeno",  # all three
    "har",  # every / each
    "pratyek",  # each / every single
    "dusra",  # other / second (masculine)
    "dusre",  # others / second (masculine plural)
    "dusri",  # other / second (feminine)
    "aanya",  # other / another
    "bahut",  # very / a lot
    "kam",  # less / little
    "adhik",  # more / excessive
    "jyada",  # more / extra
    "zyada",  # more / extra
    "thoda",  # a little / some (masculine singular)
    "thode",  # a few (masculine plural)
    "thodi",  # a little (feminine)
    "sabhi",  # all
    "poora",  # complete / whole
    "poore",  # entire (masculine plural)
    "poori",  # entire (feminine)
    "tamam",  # all / total
    "kaval",  # only / just
    "sirf",  # only / just
    "matra",  # only / merely
    "bas",  # just / stop / enough
    "tha",  # was (masculine)
    "the",  # were (masculine plural)
    "thi",  # was (feminine singular)
    "thin",  # were (feminine plural)
    "hoga",  # will be (masculine singular)
    "hoge",  # will be (masculine plural)
    "hongi",  # will be (feminine plural)
    "hogi",  # will be (feminine singular)
    "hua",  # happened / became (masculine)
    "hue",  # happened / became (plural)
    "hui",  # happened / became (feminine)
    "huin",  # happened (feminine plural)
    "raha",  # was doing / continuous (masculine)
    "rahe",  # were doing / continuous (plural)
    "rahi",  # was doing / continuous (feminine)
    "gaya",  # went / gone (masculine)
    "gaye",  # went / gone (plural)
    "gayi",  # went / gone (feminine)
    "gayein",  # went (feminine plural)
    "karna",  # to do
    "karne",  # to do (oblique/plural)
    "karni",  # to do (feminine)
    "karta",  # does / doer (masculine)
    "karte",  # do (masculine plural)
    "karti",  # does (feminine)
    "kiya",  # did (masculine)
    "kiye",  # did (plural)
    "kiyi",  # did (feminine)
    "de",  # give
    "deta",  # gives (masculine)
    "dete",  # give (plural)
    "deti",  # gives (feminine)
    "diya",  # gave (masculine)
    "diye",  # gave (plural)
    "dii",  # gave (feminine)
    "le",  # take
    "leta",  # takes (masculine)
    "lete",  # take (plural)
    "leti",  # takes (feminine)
    "liya",  # took (masculine)
    "liye",  # for / took (plural)
    "lii",  # took (feminine)
    "sakta",  # can (masculine singular)
    "sakte",  # can (masculine plural)
    "sakti",  # can (feminine)
    "chahiye",  # should / need / want
    "aaj",  # today
    "kal",  # yesterday / tomorrow
    "parson",  # day before yesterday / day after tomorrow
    "ab",  # now
    "tab",  # then / at that time
    "jab",  # when (relative pronoun)
    "kabhi",  # ever / sometime
    "sada",  # always
    "hamesha",  # always
    "phir",  # again / then
    "punah",  # again
    "phir_se",  # once again
    "baad",  # after
    "pehle",  # before / earlier
    "aage",  # ahead / forward
    "piche",  # behind / back
    "uupar",  # above / up
    "neeche",  # below / down
    "paas",  # near / close to
    "door",  # far
    "andar",  # inside
    "bahar",  # outside
    "yahan",  # here
    "vahan",  # there
    "jahan",  # where (relative pronoun)
    "kahin",  # somewhere
    "vaise",  # actually / in that manner
    "jaise",  # like / for example
    "aise",  # like this / in this way
    "vaisi",  # like that (feminine)
    "jaisi",  # like (feminine)
    "aisi",  # like this (feminine)
    "vaisa",  # like that (masculine)
    "jaisa",  # like (masculine)
    "aisa",  # like this (masculine)
    "isliye",  # therefore / so
    "kyunki",  # because
    "chunki",  # since / because
    "taki",  # so that
    "yadi",  # if
    "agar",  # if
    "to",  # then
    "varnam",  # otherwise
    "aadi",  # etc. / et cetera
    "ityadi",  # etc. / et cetera
]

# Plain list without comments/annotations
HINDI_STOPWORDS_LIST = [
    "aur",
    "hai",
    "hain",
    "ho",
    "hoon",
    "ka",
    "ke",
    "ki",
    "ko",
    "se",
    "me",
    "par",
    "tak",
    "ne",
    "bhi",
    "hi",
    "to",
    "ya",
    "lekin",
    "parantu",
    "magar",
    "kya",
    "kaun",
    "kahan",
    "kab",
    "kyun",
    "kaise",
    "kaisi",
    "kaisa",
    "kitna",
    "kitne",
    "kitni",
    "vah",
    "ve",
    "yah",
    "ye",
    "use",
    "isne",
    "usne",
    "inhoone",
    "unhoone",
    "isse",
    "usse",
    "ismein",
    "usmein",
    "iski",
    "iska",
    "iske",
    "uski",
    "uska",
    "uske",
    "unka",
    "unke",
    "unki",
    "inka",
    "inke",
    "inki",
    "main",
    "mera",
    "mere",
    "meri",
    "mujhe",
    "mujhse",
    "tum",
    "tumhara",
    "tumhare",
    "tumhari",
    "tumhe",
    "aap",
    "aapka",
    "aapke",
    "aapki",
    "aapko",
    "aapse",
    "hum",
    "hamara",
    "hamare",
    "hamari",
    "humein",
    "humse",
    "apna",
    "apne",
    "apni",
    "aapas",
    "swayam",
    "khud",
    "kuch",
    "koi",
    "sab",
    "sabhi",
    "dono",
    "teeno",
    "har",
    "pratyek",
    "dusra",
    "dusre",
    "dusri",
    "aanya",
    "bahut",
    "kam",
    "adhik",
    "jyada",
    "zyada",
    "thoda",
    "thode",
    "thodi",
    "sabhi",
    "poora",
    "poore",
    "poori",
    "tamam",
    "kaval",
    "sirf",
    "matra",
    "bas",
    "tha",
    "the",
    "thi",
    "thin",
    "hoga",
    "hoge",
    "hongi",
    "hogi",
    "hua",
    "hue",
    "hui",
    "huin",
    "raha",
    "rahe",
    "rahi",
    "gaya",
    "gaye",
    "gayi",
    "gayein",
    "karna",
    "karne",
    "karni",
    "karta",
    "karte",
    "karti",
    "kiya",
    "kiye",
    "kiyi",
    "de",
    "deta",
    "dete",
    "deti",
    "diya",
    "diye",
    "dii",
    "le",
    "leta",
    "lete",
    "leti",
    "liya",
    "liye",
    "lii",
    "sakta",
    "sakte",
    "sakti",
    "chahiye",
    "aaj",
    "kal",
    "parson",
    "ab",
    "tab",
    "jab",
    "kabhi",
    "sada",
    "hamesha",
    "phir",
    "punah",
    "phir_se",
    "baad",
    "pehle",
    "aage",
    "piche",
    "uupar",
    "neeche",
    "paas",
    "door",
    "andar",
    "bahar",
    "yahan",
    "vahan",
    "jahan",
    "kahin",
    "vaise",
    "jaise",
    "aise",
    "vaisi",
    "jaisi",
    "aisi",
    "vaisa",
    "jaisa",
    "aisa",
    "isliye",
    "kyunki",
    "chunki",
    "taki",
    "yadi",
    "agar",
    "to",
    "varnam",
    "aadi",
    "ityadi",
]


