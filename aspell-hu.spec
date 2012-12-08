%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.99.4.2-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Hungarian
%define languagecode hu
%define lc_ctype hu_HU

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.99.4.2.0
Release:       %mkrel 9
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.sourceforge.net/
#Source:	       http://prdownloads.sourceforge.net/wordlist-hu/wordlist-hu-%{src_ver}.tar.bz2
#URL:		   http://wordlist-hu.sourceforge.net
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Provides:      spell-%{languagecode}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

#cp doc/README README.%{languagecode}
#chmod 644 README Copyright README.%{languagecode}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.99.4.2.0-9mdv2011.0
+ Revision: 662838
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.4.2.0-8mdv2011.0
+ Revision: 603405
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.4.2.0-7mdv2010.1
+ Revision: 518931
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.99.4.2.0-6mdv2010.0
+ Revision: 413074
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.99.4.2.0-5mdv2009.1
+ Revision: 350037
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.99.4.2.0-4mdv2009.0
+ Revision: 220386
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.99.4.2.0-3mdv2008.1
+ Revision: 182474
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.99.4.2.0-2mdv2008.1
+ Revision: 148797
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99.4.2.0-1mdv2007.0
+ Revision: 123273
- Import aspell-hu

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99.4.2.0-1mdv2007.1
- use the mkrel macro
- disable debug packages

* Mon Feb 13 2006 Pablo Saratxaga <pablo@mandriva.com> 0.99.4.2-1mdk
- new release

* Thu Jan 13 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3-4mdk
- fix build with newer aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandriva.com> 0.3-3mdk
- allow build on ia64

